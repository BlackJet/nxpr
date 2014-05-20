KE.view.StoryView = Backbone.View.extend({
    initialize:function () {
        this.storyId = this.options['id'];
        $.ajax({
            url:'/story/' + this.storyId + '.html/',
            async:false,
            success:function(data){
                this.$el = $(data);
            }.bind(this)
        });

    },
    events:{
        'click':'close',
        'click .comment-submit':'saveComment'
    },
    render:function () {
        $('body').css('overflow','hidden');
        this.$el.prependTo('body');
        return this;
    },
    close:function (e) {
        if ($(e.target).closest('.comment-body').length) return;
        $('body').css('overflow','auto');
        this.remove();
        this.unbind();

    },
    saveComment:function(e){
        var storyId = this.storyId;
        var text = $('.comment-form textarea').val();
        var self = this;
        $.ajax({
            type:"POST",
            url:'/story/' + this.storyId + '/add_comment/',
            data:{text:text},
            success:function(response){
                if(response.success){
                     self.$el.find('.comment-form').before(response.data);


//                    var col = Backbone.Collection.extend({
//                        url:function(){
//                           return '/story/' + storyId + '/comments/';
//                        }
//
//                    });
//                    col.fetch({
//                        success:function(c,r){
//                            debugger;
//                        }
//                    });


                }
            }
        });

    }
});
