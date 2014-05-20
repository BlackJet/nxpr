KE.view.ProfileView = Backbone.View.extend({
    initialize:function (parent) {
        this.parent = $(parent);
        $.get('/profile.html/', function (data) {
            this.template = data;
            this.render();
        }.bind(this));

    },
    render:function () {
        this.$el.html(_.template(this.template));
        this.parent.html(this.$el);
        $('form[name="photoUploadForm"]').ajaxForm({
            url:'/api/profile/set_avatar/',
            beforeSubmit:null,
            success:null,
            error:null
        });

        return this;
    },
    events:{
        'click a[href="#upload"]':'openFile',
        'change input[type="file"]':'submit',
        'click #statustext':'editStatus',
        'submit #status_editor':'editStatusSubmit'
    },
    openFile:function (e) {

        e.preventDefault();
        $('input[name="photo"]').click();
        return false;

    },
    submit:function (e) {
        e.preventDefault();
        $('input[type="file"]').click();
        $('form[name="photoUploadForm"]').submit();
        return false;

    },
    editStatus:function () {
        var $text = $('#statustext');
        var blank = $text.attr('blank') == '';
        var cur_text = blank ? '' : $text.text();
        var $editor = $('#status_editor');
        $editor.find('input[name="status"]').val(cur_text);
        $editor.show().find('input[name="status"]').focus();
        $(document).mousedown(this.statusMouseDown);
    },
    editStatusSubmit:function (e) {
        e.preventDefault();
        var newText = $('#status_editor').find('input').val();
        var $text = $('#statustext');
        var curText = $text.text();
        if (curText != newText) {
            var data = $('#status_editor').serializeArray();
            $.post('/api/profile/status/',data);
            if (newText != "") {
                var blank = $text.attr('blank') == '';
                if (blank) {
                    $text.removeAttr('blank');
                }
            }
        }
        $text.text(newText);
        $('#status_editor').hide();
        $(document).off('mousedown', this.statusMouseDown);
        return false;
    },
    statusMouseDown:function (e) {
        if ($(e.target).closest('#status_editor').length) return;
        $('#status_editor').hide();
        $(document).off('mousedown', this.statusMouseDown)
    }


});
