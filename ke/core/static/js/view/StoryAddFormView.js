KE.view.StoryAddFormView = Backbone.View.extend({
    initialize:function (parent) {
        this.parent = $(parent);
        $.get('/template/story_add.html', function (data) {
            this.template = data;
            this.render();
        }.bind(this));

    },
    events:{
        'click .story-form-submit':'submit',
        'click .story-new-photo':'openFile',
        'change input[type="file"]':'previewPhoto',
        'click a[href="#addPhoto"]':'addPhoto',
        'click a[href="#deletePhoto"]':'deletePhoto'
    },
    photoTemplate:null,
    nameIndex:1,
    resetNameIndex:function () {
        var self = this;
        self.nameIndex = 1;
        $('.story-form-attachfield input[type="file"]').each(function (i, e) {
            $(e).attr('name', "photoFile" + self.nameIndex);
            $(e).siblings('input[type="text"]').attr('name', "photoTitle" + self.nameIndex);
            self.nameIndex++;
        });
    },
    deletePhoto:function (e) {
        e.preventDefault();
        var self = this;
        $(e.target).closest('.story-form-attachfield').fadeOut(500, function () {
            $(this).remove();
            self.resetNameIndex();
        });
        return false;
    },
    addPhoto:function (e) {
        e.preventDefault();
        var self = this;
        if (!self.photoTemplate) {
            $.ajax({
                url:'/template/story_new_photo.html',
                async:false,
                success:function (data) {
                    self.photoTemplate = data;
                }
            });
        }
        $(_.template(self.photoTemplate, {photo:"photoFile" + this.nameIndex, title:"photoTitle" + this.nameIndex})).insertBefore('.story-toolbar').fadeIn(500);
        this.nameIndex++;
        var scrollBottom = $(window).scrollTop() + $(window).height();
        $(window).scrollTop(scrollBottom);
        return false;
    },
    previewPhoto:function (e) {
        var input = e.target;
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            var $image = $('.story-new-photo', $(e.target).closest('.story-form-attachfield'));
            reader.onload = function (e) {
                $image.attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    },
    submit:function (e) {
        $('form[name="storyForm"]').submit();
    },
    openFile:function (e) {
        $('input[type="file"]', $(e.target).closest('.story-form-attachfield')).click();
    },
    render:function () {
        this.$el.html(_.template(this.template));
        this.parent.html(this.$el);
        $('form[name="storyForm"]').ajaxForm({
            url:'/api/story/add/',
            beforeSubmit:null,
            success:null,
            error:null
        });
        return this;
    }


});
