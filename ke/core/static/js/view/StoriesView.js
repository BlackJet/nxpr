KE.view.StoriesView = Backbone.View.extend({
    page:1,
    total: null,
    finished:false,
    isLoading:false,
    url:'/story.html/',
    initialize:function (parent) {

        this.$parent = $(parent);
        $.ajax({
            url:this.url,
            async:false,
            success:function(data){
                this.$el = $(data);
                this.render();
            }.bind(this)
        });

        $(window).scroll(this.checkScroll.bind(this));
    },
    events:{
        'click .story-open':'more',
        'click #nextStoryPage':'addNextPage',
        'click .story-upvote' :'vote',
        'click .story-downvote' :'vote',
        'click a[href="#story-comment"]' :'openStory'
    },
    getStoryId:function(e){
        var block = $(e.target).closest('.story-block');
        return parseInt(block.find('input[type="hidden"]').val());
    },
    openStory:function(e){
        var id = this.getStoryId(e);
        var sv = new KE.view.StoryView({id:id});
        sv.render();
        e.preventDefault();
        return false;
    },
    checkScroll: function () {
        if( !this.isLoading && ($(window).scrollTop() > ($(document).height() -$(window).height() -  500) )) {
            this.addNextPage();
        }
    },
    render:function () {
        this.$parent.html(this.$el);
        this.total = parseInt($('#stories').children('input[type="hidden"]').val());
        return this;
    },
    more:function (e) {
        var block = $(e.target).parents('.story-block');
        if (!block.find('.story-content').length) {
            $(e.target).css("background-image", "url(/static/img/hide_pic.png)");

            var storyId = block.find('input[type="hidden"]').val();
            $.get('/story/' + storyId + '/attachments.html/', function (html) {
                $(html).appendTo(block);
            })
        }
        else {
            $(e.target).css("background-image", "url(/static/img/show_pic.png)");
            block.find('.story-content').remove();
        }
    },
    addNextPage:function(){
        if(this.finished){
            console.log("finished");
            return;
        }
        this.isLoading = true;

        var self = this;
        this.page++;
        $.get('/story.html/?page=' + this.page + '&total=' +this.total, function(html){
            $(html).appendTo($('.story-list'));
            self.isLoading = false;
        }).error(function(){ self.finished = true; self.isLoading = false;});

    },
    vote:function(e){
        var value = 1;
        if($(e.target).hasClass('arrow-clicked')) return;
        if($(e.target).is('.story-downvote')) value = -1;
        var block = $(e.target).closest('.story-block');
        var storyId = block.find('input[type="hidden"]').val();
        $.post('/api/story/' + storyId + '/vote/',{value:value},function(data){
            if(!data.success) return;
            var newRate = parseInt(block.find('.rate').text()) + value;
            block.find('.rate').text(newRate);
            if(newRate != 0){
                $(e.target).addClass('arrow-clicked');
            }
            $(e.target).siblings().removeClass('arrow-clicked');

        });


    }



});
