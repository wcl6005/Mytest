$(function() {

    var vm = new Vue({
        el: '#form-signin',
        data: {
            email: '',
            password: '',
            remember: false
        },
        methods: {
            submit: function (event) {
                event.preventDefault();
                var email = this.email.trim().toLowerCase();
                showError();
                startLoading();
                postApi('/api/signin', { //调用、edustack/apis/api.py 
                                         // api_res.add_resource(API_Auth, '/signin')
                    email: email,
                    password: CryptoJS.MD5(this.password).toString(),
                    remember: this.remember
                }, function (err, result) {
                    if (err) {
                        showError(err);
                    }
                    else {
                        //return location.assign(result.admin ? '/manage/' : '/');//重新定位到后台
                        return location.assign('/'); 
                        //alert(href);
                    }
                    stopLoading();
                });
            }
        }
    });
})
