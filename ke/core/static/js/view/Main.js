KE.view.Main = Backbone.View.extend({
    events : {
        'click #logout' : 'logout'
    },
    logout:function (e) {
        $.ajax({
            url:'/api/logout/',
            async:false
        });
    }

});
