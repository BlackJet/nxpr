KE.view.RegForm = Backbone.View.extend({
    initialize:function(parent){
        this.parent = $(parent)
        $.get('/register.html/', function(data){
            this.template  = data;
            this.render();
        }.bind(this));

    },
    render:function(){
        this.$el.html(_.template(this.template));
        this.parent.html(this.$el);
        return this;
    },
	events : {
		'click .b-reg-form-submit' : 'submit'
    },
	submit : function(e){
        e.preventDefault();
        var processData = function(feed) {
            if (feed.success == true) {
                Backbone.history.navigate('/profile/',{trigger:true});
            }
            else {
                var errors = feed.errors;
                for (var i = 0; i < errors.length; i++) {
                    var field = errors[i];
                    var inputName = field[0];
                    var message = field[1];
                    $('input[name="' + inputName + '"]')
                        .addClass("input-invalid")
                        .siblings(".text-error").text(message)
                        .parent().prev().addClass("text-error");
                }

            }
        };
        var setDefaultForm = function() {
            $(".form-field-label")
                .removeClass("text-error")
                .siblings(".form-field-input").children("input").removeClass("input-invalid")
                .siblings(".text-error").text("");

        }
        var formData = $("#regForm .form").serializeArray();
        $.post('/api/profile/add/', formData, processData);
        return false;
	}


});
