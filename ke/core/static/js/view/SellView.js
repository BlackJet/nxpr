KE.view.SellView = Backbone.View.extend({

    url:'/sell.html/',
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

    },
    events:{
        'click button':'submit'
    },
    render:function () {
        this.$parent.html(this.$el);
        return this;
    },
    submit:function (e) {
        e.preventDefault();
        var form = $('form[name="profile_edit"]');
        $.post(form.attr('action'), form.serializeArray());
        return false;
    }
});
