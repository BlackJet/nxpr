KE.view.AuthForm = Backbone.View.extend({
    el:'#authForm',
	events : {
		'click .b-auth-submit' : 'submit'
    },
	submit : function(e){
        debugger;
        var formData = $("#authForm .b-auth").serializeArray();
        $.post('/api/login/', formData, function(response){
            if(response.success == true){
                window.location.reload();
                window.userLogined = true;
            }
        });
        e.preventDefault();
        return false;
    }

});
