KE.view.User = Backbone.View.extend({
    className:'widget',
	tagName : 'div',
	model : new KE.model.User(),
	
	initialize : function(parent) {
		this.model.bind('change', this.render, this);
        this.parent = $(parent);
        this.render();
	},

	render : function() {
//		var compiledTemplate = _.template($('#teamTemplate').html());
//		$(this.el).html(compiledTemplate(this.model.toJSON()));

        $(this.el).html("We are the champions<div class='me'>ME</div>");
        this.parent.append(this.el);
	},
	events : {
		'click .me' : 'moreInfo'
	},
	
	moreInfo : function(e){
        var html = _.template('<span>{{ name }}</span>', { name: 'John Smith' });
        $(".me").html(html);
		// Logic here
	}

});
