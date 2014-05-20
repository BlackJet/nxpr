/**
 * profile.main
 */
ke.apps.profile = {
    init:function() {
    },
    showEditPage:function() {
        $.get('profile/edit', null, function(html) {
            Utils.loadPage(html);
        });
    },
    show:function() {
        $.get('profile/main', null, function(html) {
            Utils.loadPage(html);
        });
    }

}



