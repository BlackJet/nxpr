/**
 * account.main
 */
ke.apps.account = {
    init:function() {
        if (!this.isUserLogined()) {
            this.showAuthForm();
        }

    },
    showRegForm:function() {
        $.ajax({
            url: "account/form/reg",
            type: "GET",
            cache: false,
            success: function (html) {
                $('.h-center').html(html);
                $('.b-auth').css({'display':'display'});
            }
        });
    },
    showRegCongratulationPage:function() {
        $.ajax({
            url: "account/page/reg_congratulation",
            type: "GET",
            cache: false,
            success: function (html) {
                $('.h-center').html(html);
            }
        });
    },
    isUserLogined:function() {
        var logined = false;
        $.ajax({
            url: "account/isUserLogined",
            dataType:'json',
            async:false,
            type: "GET",
            success: function(json) {
                if (json.success) logined = true;
            }
        });
        return logined;
    },
    showRegForm:function() {
        $.ajax({
            url: "account/form/reg",
            type: "GET",
            cache: false,
            success: function (html) {
                $('.h-center').html(html);
                $('.b-auth').css({'display':'display'});
            }
        });
    },
    showAuthForm:function() {
        $.ajax({
            url: "account/form/auth",
            type: "GET",
            cache: false,
            success: function (html) {
                $('.l-header-center').html(html);
            }
        });

    },
    hideAuthForm:function() {
        $('.b-auth').css({'display':'none'});
    }

}
