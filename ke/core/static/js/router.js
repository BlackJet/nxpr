KE.Router= Backbone.Router.extend({

	routes : {
		'': "index",
		'teams/' : "teams",
        'profile/' :'profile',
        'story/' :'story',
        'story_add/' :'storyAdd',
        'sell/' :'sell',
        'profile_edit/' :'editProfile',
        'register/' :'register',
		"/teams/:country" : "getTeamsCountry",
		"/teams/:country/:name" : "getTeam",
		"*error" : "fourOfour"
	},

	index: function(a){
        console.log("/index/");
    },

    profile:function(){
        new KE.view.ProfileView('.h-center');
    },
    story:function(){
        new KE.view.StoriesView('.h-center');
    },
    storyAdd:function(){
        new KE.view.StoryAddFormView('.h-center');
    },
    editProfile:function(){
        new KE.view.ProfileEditView('.h-center');
    },
    register:function(e){
        new KE.view.RegForm('.h-center');
    },
    sell:function(e){
        new KE.view.SellView('.h-center');
    },

    teams: function() {
        console.log('getTeams');
        return false;
		// List all teams 
	},
	getTeamsCountry: function(country) {
		// Get list of teams for specific country
	},
	getTeam: function(country, name) {
		// Get the teams for a specific country and with a specific name
	},	
	fourOfour: function(error) {
		// 404 page
	}
});
