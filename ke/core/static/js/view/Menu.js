KE.view.Menu = Backbone.View.extend({
    el:'.h-nav',
    events:{
        'click a[href="/profile/"]':'showProfile',
        'click a[href="/profile_edit/"]':'profileEdit',
        'click a[href="/story/"]':'showStories',
        'click a[href="/story_add/"]':'showAddStoryForm',
        'click a[href="/sell/"]':'showSellView'

    },
    showProfile:function (e) {
        var p = new KE.view.ProfileView('.h-center');
        Backbone.history.navigate('/profile/',{trigger: false});
        e.preventDefault();
        return false;
    },
    profileEdit:function (e) {
        pev = new KE.view.ProfileEditView('.h-center');
        Backbone.history.navigate('/profile_edit/',{trigger: false});
        e.preventDefault();
        return false;
    },
    showAddStoryForm: function(e){
        Backbone.history.navigate('/story_add/',{trigger: true});
        var p = new KE.view.StoryAddFormView('.h-center');
        e.preventDefault();
        return false;
    },

    showStories:function (e) {
        var p = new KE.view.StoriesView('.h-center');
        Backbone.history.navigate('/story/',{trigger: false});
        e.preventDefault();
        return false;
    },

    showSellView:function (e) {
        new KE.view.SellView('.h-center');
        Backbone.history.navigate('/sell/',{trigger: false});
        e.preventDefault();
        return false;
    }


});
//    showProfile:function (e) {
//        e.preventDefault();
//        var activeView = this.activeView;
//        var hash = e.target.hash.replace(/^.*#/, '');
//        if (document.getElementById(hash))
//            if (activeView == "#" + hash) {
//                return false;
//            }
//            else {
//                $(activeView).toggle();
//                $("#" + hash).toggle();
//                this.activeView = "#" + hash;
//            }
//        else {
//            if (activeView) $(activeView).toggle();
//            $.get(hash, null, function (page) {
//                $('.h-center').append(page);
//                this.activeView = '#' + hash;
//            }.bind(this));
//        }
//        return false;
//
//    }