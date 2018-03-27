$(function(){
	
	
	    var $category = $('.open-cot > li:gt(5)'); 
		$category.hide();
		$(".open-add").click(function(){
			var $a=$('.open-cot > li:gt(5)');
				$a.stop().slideDown(500)
			})
	    $(".open-reduce").click(function(){
			var $a=$('.open-cot > li:gt(5)');
				$a.stop().slideUp(500)
			})

	$(".fl-open").click(function(){
		$(".frindlink").show()
		return false;
		})
	  $(".retop").click(function(){
		$('body,html').animate({scrollTop:0},300);
		return false;
		});
	$(".dropdown-btn").click(function(){
		var $a=$(this).parents(".parent")
		var $b=$a.find(".dropdown")
		if($b.is(":visible")){
			$b.stop().slideUp(300)
			$(this).removeClass("open")
		}
		else{
		$(this).addClass("open");
		$a.find(".dropdown").stop().slideDown(300);
		$a.siblings().find(".dropdown").stop().slideUp(300);
		$a.siblings().find(".ldfw-item .ldfw-txt .rmore").removeClass("open");
			}
		})
      $('.gn-box .panel-collapse').on('hide.bs.collapse', function () {
	    $(this).parent().find("div a span").addClass("caret-top").removeClass("caret")
	  })
      $('.gn-box .panel-collapse').on('show.bs.collapse', function () {
	    $(this).parent().find("div a span").addClass("caret").removeClass("caret-top")
	  })
	  
      $('#flink').on('hide.bs.collapse', function () {
	    $('#open-flink').text("友情链接展开")
	  })
      $('#flink').on('show.bs.collapse', function () {
	    $('#open-flink').text("友情链接隐藏")
	  })
	  
	  
	  $(".foctxt input[type='text']:input,.foctxt textarea:input").focus(function(){
			  $(this).addClass("focus");
			  if($(this).val() ==this.defaultValue){  
                  $(this).val("");
				  $(this).css("color","#555")           
			  } 
		}).blur(function(){
			 $(this).removeClass("focus");
			 if ($(this).val() == '') {
                $(this).val(this.defaultValue);
				  $(this).css("color","#999")           
             }
		});
      $(".dd-checkedall").click(function(){
			var $a=$(this).parents(".dd-selecCot").find("input.dd-input")
			if(this.checked){
				 $a.prop("checked", true );
			}else{								
			     $a.prop("checked", false );
			}
			 })
	 
	  $('.dd-selecCot input.dd-input').click(function(){
		       var $b=$(this).parents(".dd-selecCot").find(".dd-checkedall")
			   var flag=true;
               $('.dd-selecCot input.dd-input').each(function(){
					if(!this.checked){
						 flag = false;
					}
			   });

			   if( flag ){
					 $b.prop('checked', true );
			   }else{
					 $b.prop('checked', false );
			   }
	 });
	$(".dd-qx").click(function(){
		 $(".dd-checkedall").trigger("click")
	});

	/**
	 * 通用登录
	 */
	//注释 添加  回车提交 功能。2016/09/19
	$('#min_loginfrom').submit(function(){
		  $('.hlogsub').click();
		  return false;
	});	 
	$('.hlogsub').click(function() {
		var mobile = $.trim($('.hlogmobile').val());
		var pass = $.trim($('.hlogpass').val());
		var errmeg = $('.headregerrmeg');
		if(!mobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.addClass('headregerrmegbg');
			errmeg.text('请您正确输入手机号码');
			window.setTimeout(function(){errmeg.text('')},2500);
			return;
		}
		if(pass.length < 6){
			errmeg.addClass('headregerrmegbg');
			errmeg.text('您输入的密码不能少于6位');
			window.setTimeout(function(){errmeg.text('')},2500);
			return;
		}
		if(pass.length > 20){
			errmeg.addClass('headregerrmegbg');
			errmeg.text('您输入的密码不能超过20位');
			window.setTimeout(function(){errmeg.text('')},2500);
			return;
		}
		$.ajax({
			url: _host + '/Qyzsweb/dolog',
			type: 'post',
			dataType: 'json',
			data:{
				mobile: mobile,
				pass: pass,
			},
			success: function(data){
				if(data.type == 1){
					//window.location.href = '/Home/pay/lists';
					var url = $('#gotourl').val();
					//alert(url);
					if(url!=''){
					    window.location.href = url;
					}else{ 
						var str = '<div class="user-info dropdown" style="font-size: 14px;">\
			                  <a href="/Member/Orders/index" style="width: 62px;height: 61px;display: block;position: absolute;top:10px;left:50px;z-index: 200;"></a>\
			                  <div data-toggle="dropdown" data-hover="dropdown">\
			                      <img  src="images/default_tpic.png"  width="62" height="61" style="border-radius: 50%;">\
			                      <p>'+data.nickname+'</p>\
			                  </div>\
			                  <ul class="dropdown-menu" >\
			                      <li class="sj"></li>\
			                      <li><a href="__APP__/Member/Allorders">我的订单</a></li>\
			                      <li><a href="/Pay/lists">我的清单</a></li>\
			                      <li><a href="__APP__/Member/Mescenter">消息中心</a></li>\
			                      <li><a class="logouted" href="javascript:;">退出</a></li>\
			                  </ul>\
			              </div>';
						var strs = '<a href="javascript:;" class="gn-btn mb10 opacity gnbg gpay">去结算</a>';
						var $b=$(".dropdown");
						$('.dropdown').hover(function(){
							$(this).addClass("open");
							
						},function(){
							  $(this).removeClass("open");
						})
						$('.login-box').before(str);
						$('#qujiesuan').before(strs);
						addlogouted();
						gotopays();
						$('.login-box').remove(); 
						$('#qujiesuan').remove();
						
						$('#dolog').modal('hide');
						
					}
				}else if(data.type == 2){
					errmeg.addClass('headregerrmegbg');
					errmeg.text('请您正确输入手机号码');
					window.setTimeout(function(){errmeg.text('')},2500);
					return;
				}else if(data.type == 3){
					errmeg.addClass('headregerrmegbg');
					errmeg.text('您输入的手机号不存在');
					window.setTimeout(function(){errmeg.text('')},2500);
					return;
				}else if(data.type == 4){
					errmeg.addClass('headregerrmegbg');
					errmeg.text('手机号码和密码不匹配');
					window.setTimeout(function(){errmeg.text('')},2500);
					return;
				}
			}
		});
	});
	
	
	/*结算
	 * */ 
	var gotopays = function(){
	 $('.gpay').click(function() {
	        var _this = $(this);
	        var errmeg = $('.levitated');
	        // 网站分类
	        var wzfl = $('#wzfl-sel').find('ul').find('.active').text();
	        // 终端分类
	        var zdfl = Array();
	        $('#zdfl-sel').find('zd').each(function(k, v) {
	            if($(this).find('label').attr('class') == 'checked'){
	                zdfl[k] = $(this).find('label').attr('name');
	            }
	        }); 
	        // 基础功能
	        var jcgn = Array();
	        var kzgn = Array();
	        var hyjc = Array();
	        var hyhz = Array();
	        // 基础功能
	        $('#jcgn-check').find('ul li').each(function(k, v) {
	            if($(this).find('label').attr('class') == 'checked'){
	                jcgn[k] = $(this).find('label').text();
	            }
	        });
	        // 扩展功能
	        $('.kzgn-check').find('ul li').each(function(k, v) {
	            if($(this).find('label').attr('class') == 'checked'){
	                kzgn[k] = $(this).find('label').text();
	            }
	        });
	        // 会员基础
	        $('#hyjc-check').find('ul li').each(function(k, v) {
	            if($(this).find('label').attr('class') == 'checked'){
	                hyjc[k] = $(this).find('label').text();
	            }
	        });
	        // 会员扩展
	        $('#hyhz-check').find('ul li').each(function(k, v) {
	            if($(this).find('label').attr('class') == 'checked'){
	                hyhz[k] = $(this).find('label').text();
	            }
	        });
	        // 产品id
	        var proid = parseInt($('.proname').attr('pid'));
	        // 产品名称
	        var proname = $('.proname').text();
	        // 产品总价
	        var totalprice = parseInt($('#totalPrice').text());
	        // 产品原价
	        var orgprice = parseInt($('#costPrice').text());
	        if(proid == '' || proid == undefined || proname == '' || proname == undefined){
	            errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('产品类型不正确，请联系客服！');
	            return;
	        }
	        if(proid != 3 && wzfl == ''){
	            errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确选择网站分类，或者有任何疑问请您联系客服！');
	            return;
	        }
	        if(zdfl == '' || zdfl == undefined){
	            errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确选择终端分类，或者有任何疑问请您联系客服！');
	            return;
	        }
	        $.ajax({
	            url: _host + '/Qyzsweb/gocar',
	            type: 'POST',
	            dataType: 'json',
	            data: {
	                proid: proid, // 产品id
	                proname: proname, // 产品名称
	                wzfl: wzfl, // 网站分类
	                zdfl: zdfl, // 终端分类
	                jcgn: jcgn, // 基础功能
	                kzgn: kzgn, // 扩展功能
	                hyjc: hyjc, // 会员基础
	                hyhz: hyhz, // 会员扩展
	                orgprice: orgprice, // 产品原价格
	                totalprice: totalprice, // 产品价格
	            },
	            success: function(data){
	                if(data.type == 1){
	                    // location.href = _host + "/Pay/lists";
	                    _this.parent().find('input').val(data.id);
	                    _this.parent('form').submit();
	                    // location.href = _host + "/Pay/index/"+data.id;
	                }else if(data.type == 2){
	                    errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('保存清单失败，请稍后再试，或者联系客服！');
	                    return;
	                }else if(data.type == 3){
	                    errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确选择信息，或稍后再试，如果有疑问，请联系客服！');
	                    return;
	                }else if(data.type == 4){
	                    errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('添加清单失败，请稍后再试，或者联系客服！');
	                    return;
	                }else if(data.type == 5){
	                    errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('更新清单失败，请稍后再试，或者联系客服！');
	                    return;
	                }else{
	                    errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('未知错误，请联系客服！');
	                    return;
	                }
	            }
	        }); 
	    });
	}
	gotopays();
	/**
	 * [退出登录]
	 * @param  {[type]} ) {			}       [description]
	 * @return {[type]}   [description]
	 */
var addlogouted=function(){	
	$('.logouted').click(function() {
		var errmeg = $('.levitatedlogout');
		$.ajax({
			url: _host + '/Login/logout',
			type: 'post',
			dataType: 'json',
			data: {
				log: 'log'
			},
			success: function(data){
				if(data.type == 1){
					var str = '<div class="login-box pull-right clearfix">\
								<a href="'+_host+'/Home/Login/index">登录</a>\
								<a href="'+_host+'/Home/Register/index">注册</a>\
								</div>';
					$('.user-info').before(str);
					$('.user-info').remove();
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow',function(){window.location.href=window.location.href})},100)}).text('退出成功！');
				}else if(data.type == 2){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('异常操作，请稍后再试！');
					return;
				}
			}
		});
	});
};
addlogouted();
//未开启会员注册
	$('.register').click(function() {
		var errmeg = $('.levitatedlogout');
		errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('很遗憾，我们暂时没有开放会员注册！');
	});
	/**
	 * 页面底部微信 qq 邮箱
	 */
	// 微信
	$('.txtag-wx').hover(function(){$(this).addClass('tx-1');$(this).find('div').show();},function(){$(this).removeClass('tx-1');$(this).find('div').hide()});
	// 邮箱
	$('.txtag-em').hover(function(){$(this).addClass('tx-2');},function(){$(this).removeClass('tx-2');});
	// qq
	$('.lianxisedqq').hover(function(){$('.txtag-qq').addClass('tx-3');},function(){$('.txtag-qq').removeClass('tx-3');});
	// 显示邮件订阅层
	$('.txtag-em').click(function(){$('.dyemail').fadeIn('slow')});
	// 关闭邮件订阅层
	$('.dyclose').click(function(){$('.dyemail').fadeOut('slow')});

	$('.btn-darkblueem').click(function() {
		var errmeg = $('.levitated');
		var email = $.trim($(this).parent().parent().find('div').find('input').val());
		if(!email.match(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入邮箱地址！');
			return;
		}
		$.ajax({
			url: _host + '/Home/Appdevelop/dyemail',
			type: 'post',
			dataType: 'json',
			data: {
				email: email
			},
			success: function(data){
				if(data.type == 1){
					$('.dyemail').fadeOut('slow');
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('订阅成功');
				}else if(data.type == 2){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('邮箱地址不能为空！');
					return;
				}else if(data.type == 3){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('订阅失败！101');
					return;
				}else if(data.type == 4){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('订阅失败！102');
					return;
				}else if(data.type == 5){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('邮箱与现订阅邮箱相同！');
					return;
				}else if(data.type == 6){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('订阅失败！103');
					return;
				}
			}
		});
		
	});
	/**
	 * 意见反馈
	 */
	$('.fkcontent').change(function() {
		var fkcontent = $.trim($(this).val());
		var errmeg = $('.levitated');
		if(fkcontent.length < 5){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('亲，我还不太明白您的意思哦！多说两句吧！');
			return;
		}
	});
	$('.fkmobile').change(function() {
		var fkmobile = $.trim($(this).val());
		var errmeg = $('.levitated');
		if(fkmobile != '' && !fkmobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入手机号码！');
			return;
		}
	});
	// 意见反馈提交
	$('.container').on('click', '.fkfeedbaksub', function() {
		var fkcontent = $.trim($('.fkcontent').val());
		var fkmobile = $.trim($('.fkmobile').val());
		var fktype = $.trim($('.fktype option:selected').val());
		var fkname = $.trim($('.fkname').val());
		var fkqq = $.trim($('.fkqq').val());
		var fkimgs = '';
		var errmeg = $('.levitated');
		$('.fkimgs').each(function(k, v) {
			fkimgs += $(this).find('div').find('input').val() + '|';
		});
		if(fkcontent == '' && fkimgs==''){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('反馈内容和附件不得同时为空！');
			return;
		}
		if(fkmobile != '' && !fkmobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入手机号码！');
			return;
		}
		if(fkcontent != '' && fkcontent.length < 5){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('亲，我还不太明白您的意思哦！多说两句吧！');
			return;
		}
		$.ajax({
			url: _host + '/Appdevelop/feedbackedd',
			type: 'post',
			dataType: 'json',
			data: {
				fktype: fktype,
				fkcontent: fkcontent,
				fkname: fkname,
				fkmobile: fkmobile,
				fkqq: fkqq,
				fkimgs: fkimgs,
			},
			success: function(data){
				if(data.type == 1){
					$('#myInfoModal').modal('show');
					window.setTimeout(function(){location.href = '/'},3000);
				}else if(data.type == 2){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('添加失败，请稍后再试或联系客服！');
					return;
				}
			}
		});
	});

	/**
	 * [反馈意见]
	 * @param  {[type]} ) {		var       fdname [description]
	 * @return {[type]}   [description]
	 */
	$('.feedbacksub').click(function() {
		var fdname = $('.fdname').val();
		var fdemail = $('.fdemail').val();
		var fdmobile = $('.fdmobile').val();
		var fdcontent = $('.fdcontent').val();
		var errmeg = $('.levitated');
		var myInfoModal = $('#myInfoModal');
		if(fdmobile != '' && !fdmobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入手机号码！');
			return;
		}
		if(fdemail != '' && !fdemail.match(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入邮箱地址！');
			return;
		}
		if(fdcontent.length < 5){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('亲，我还不太明白您的意思哦！多说两句吧！');
			return;
		}
		$.ajax({
			url: _host + '/Appdevelop/feedbacks',
			type: 'POST',
			dataType: 'json',
			data: {
				fdname: fdname,
				fdemail: fdemail,
				fdmobile: fdmobile,
				fdcontent: fdcontent,
			},
			success: function(data){
				if(data.type == 1){
					//myInfoModal.modal('show');
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('提交成功，感谢您的留言！');
					//window.setTimeout(function(){window.location.href=window.location.href},3000); //提交完刷新当前页
					$("input[type=reset]").trigger("click");
				}else if(data.type == 2){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请填写完整信息之后再提交！');
				}else if(data.type == 3){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('添加失败，请稍后再试或联系客服！');
				}
			}
			
		});
		
	});

	/**
	 * [点击刷新验证码]
	 * @param  {[type]} ) {		var       _this [description]
	 * @return {[type]}   [description]
	 */
	$('.freshver').click(function() {
		var _this = $(this);
		var src = _this.attr('src');
		_this.attr("src",chgUrl(src));
	});

	function chgUrl(url){
		var timestamp = (new Date()).valueOf();
		// url = url.substring(0,21);

		if((url.indexOf("&")>=0)){
			url = url + "×tamp=" + timestamp;
		}else{
			url = url + "?timestamp=" + timestamp;
		}
		return url;
	}

	/**
	 * [提交注册]
	 * @param  {[type]} ) {		var       _this [description]
	 * @return {[type]}   [description]
	 */
	// 手机验证
	$('.regmob').change(function() {
		var regmob = $(this).val();
		var errmeg = $(this).parent().find('.logerrmeg');
		if(!regmob.match(/^1[34578]{1}\d{9}$/)){
			errmeg.text('请您正确输入手机号码');
			return;
		}
		$.ajax({
			url: _host + '/Register/getmob',
			type: 'post',
			dataType: 'json',
			data: {
				mobile: regmob
			},
			success: function(data){
				if(data.type == 1){
					errmeg.text('');
				}else if(data.type == 2){
					errmeg.text('请您输入正确手机号码');
					return;
				}else if(data.type == 3){
					errmeg.text('您输入的手机号已存在');
					return;
				}
			}
		});
	});

	// 图形验证码
	$('.imgcode').change(function() {
		var imgcode = $.trim($(this).val());
		var errmeg = $(this).parent().find('.logerrmeg');
		if(imgcode.length != 4){
			errmeg.text('请输入四位图形验证码');
			return false;
		}else{
			errmeg.text('');
		}
	});
	// 获取手机验证码
	$('.getmeg').click(function() {
		var _this = $(this);
		var regmob = $('.regmob').val();
		var imgcode = $.trim($('.imgcode').val());
		var regmoberr = $('.regmob').parent().find('.logerrmeg');
		var imgcodeerr = $('.imgcode').parent().find('.logerrmeg');
		var errmeg = $(this).parent().parent().find('div').find('div').find('.logerrmeg');
		if(regmoberr.text() != ''){
			// errmeg.text('请您输入正确的手机号码');
			return false;
		}
		if(!regmob.match(/^1[34578]{1}\d{9}$/)){
			regmoberr.text('请您正确输入手机号码');
			return false;
		}
		if(imgcodeerr.text() != ''){
			return false;
		}
		$.ajax({
			url: _host + '/Register/getimgcode',
			type: 'post',
			dataType: 'json',
			data: {
				imgcode: imgcode
			},
			success: function(data){
				if(data.type == 1){
					imgcodeerr.text('');
					$.ajax({
						url: _host + '/Register/getmeg',
						type: 'post',
						dataType: 'json',
						data: {
							meg: 'meg',
							regmob: regmob,
						},
						success: function(data){
							if(data.type == 1){
								_this.attr('disabled','disabled');
								_this.css({background: '#FFEEDD'});
								_this.html('<st>60</st>s后再次获取');
								var st = _this.find('st');
								var i = 59;
								var timer = setInterval(function(){
									if(i < 0) {
										_this.text('获取短信验证码');
										_this.css({background: 'white'});
										_this.removeAttr('disabled');
										clearInterval(timer);
									}else{
										st.text(i--);
									}
								},1000);
								var src = $('.freshver').attr('src');
								$('.freshver').attr("src",chgUrl(src));
								return;
							}else if(data.type == 2){
								errmeg.text('异常访问，请稍后再试');
								window.setTimeout(function(){errmeg.text('')},3000);
								return;
							}else if(data.type == 3){
								errmeg.text(data.error);
								window.setTimeout(function(){errmeg.text('')},3000);
								return;
							}
						}
					});
				}else if(data.type == 2){
					imgcodeerr.text('图形验证码不正确');
					return false;
				}
			}
		});
	});

	// 手机验证码
	$('.mobcode').change(function() {
		var mobcode = $(this).val();
		var errmeg = $(this).parent().find('.logerrmeg');
		if(mobcode.length != 6){
			errmeg.text('请输入六位手机验证码');
			return;
		}else{
			errmeg.text('');
		}
		$.ajax({
			url: _host + '/Register/getmegmeg',
			type: 'post',
			dataType: 'json',
			data: {
				mobcode: mobcode
			},
			success: function(data){
				if(data.type == 1){
					errmeg.text('');
				}else if(data.type == 2){
					errmeg.text('手机验证码已超时，请重新获取');
					return;
				}else if(data.type == 3){
					errmeg.text('手机验证码已超时，请重新获取');
					return;
				}else if(data.type == 4){
					errmeg.text('手机验证码不正确');
					return;
				}
			}
		});
	});

	// 验证密码
	$('.regpass').change(function() {
		var regpass = $.trim($(this).val());
		var errmeg = $(this).parent().find('.logerrmeg');
		if(regpass == ''){
			errmeg.text('密码不能为空');
			return;
		}
		if(regpass.length < 6){
			errmeg.text('6-20位大小写英文字母、符号或数字组合');
			return;
		}
		if(regpass.length > 20){
			errmeg.text('6-20位大小写英文字母、符号或数字组合');
			return;
		}
		errmeg.text('');
	});
	// 确认密码
	$('.regsupa').change(function() {
		var regpass = $.trim($('.regpass').val());
		var regsupa = $.trim($(this).val());
		var errmeg = $(this).parent().find('.logerrmeg');
		if(regsupa == ''){
			errmeg.text('确认密码不能为空');
			return;
		}
		if(regsupa.length < 6){
			errmeg.text('6-20位大小写英文字母、符号或数字组合');
			return;
		}
		if(regsupa.length > 20){
			errmeg.text('6-20位大小写英文字母、符号或数字组合');
			return;
		}
		errmeg.text('');
	});
	// 提交注册
	$('.regsub').click(function() {
		var _this = $(this);
		var regmob = $.trim($('.regmob').val());
		var imgcode = $.trim($('.imgcode').val());
		var mobcode = $.trim($('.mobcode').val());
		var regpass = $.trim($('.regpass').val());
		var regsupa = $.trim($('.regsupa').val());
		var regxieyi = $('.regxieyi:checked').val();
		var regmoberr = $('.regmob').parent().find('.logerrmeg');
		var imgcodeerr = $('.imgcode').parent().find('.logerrmeg');
		var mobcodeerr = $('.mobcode').parent().find('.logerrmeg');
		var regpasserr = $('.regpass').parent().find('.logerrmeg');
		var regsupaerr = $('.regsupa').parent().find('.logerrmeg');
		var regxieyierr = $('.regxieyi').parent().parent().parent().find('.logerrmeg');
		// 手机
		if(regmoberr.text() != ''){
			// errmeg.text('请您正确输入手机号码');
			return;
		}
		if(!regmob.match(/^1[34578]{1}\d{9}$/)){
			regmoberr.text('请您正确输入手机号码');
			return;
		}
		// 手机验证码
		if(mobcodeerr.text() != ''){
			// errmeg.text('请输入六位手机验证码');
			return;
		}
		// 密码
		if(regpasserr.text() != ''){
			// regpasserr.text('请正确输入密码');
			return;
		}
		if(regpass == ''){
			regpasserr.text('密码不能为空');
			return;
		}
		// 确认密码
		if(regsupaerr.text() != ''){
			// errmeg.text('请正确输入确认密码');
			return;
		}
		if(regsupa == ''){
			regsupaerr.text('确认密码不能为空');
			return;
		}
		if(regpass != regsupa){
			regsupaerr.text('密码和确认密码不一致');
			return;
		}
		// 同意协议
		if(regxieyi == '' || regxieyi != 1){
			regxieyierr.text('请您先阅读有关条款，并同意遵守协议');
			setTimeout(function(){regxieyierr.text('')},2500);
			return;
		}
		$.ajax({
			url: _host + '/Register/getmob',
			type: 'post',
			dataType: 'json',
			data: {
				mobile: regmob
			},
			success: function(data){
				if(data.type == 1){
					$.ajax({
						url: _host + '/Register/getmegmeg',
						type: 'post',
						dataType: 'json',
						data: {
							mobcode: mobcode
						},
						success: function(data){
							if(data.type == 1){
								$('form').submit();
							}else if(data.type == 2){
								mobcodeerr.text('手机验证码已超时，请重新获取');
								return;
							}else if(data.type == 3){
								mobcodeerr.text('手机验证码已超时，请重新获取');
								return;
							}else if(data.type == 4){
								mobcodeerr.text('手机验证码不正确');
								return;
							}
						}
					});
				}else if(data.type == 2){
					regmoberr.text('请您输入正确手机号码');
					return;
				}else if(data.type == 3){
					regmoberr.text('您输入的手机号已存在');
					return;
				}
			}
		});
	});

	/**
	 * [提交登录]
	 * @param  {[type]} ) {		var       _this [description]
	 * @return {[type]}   [description]
	 */
	// 手机判断
	$('.logmobile').change(function() {
		var mobile = $(this).val();
		var errmeg = $(this).parent().find('.logerrmeg');
		if(!mobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.text('请您正确输入手机号码');
			return;
		}
		errmeg.text('');
		$.ajax({
			url: _host + '/Login/getmobile',
			type: 'post',
			dataType: 'json',
			data: {
				mobile: mobile
			},
			success: function(data){
				if(data.type == 1){
					errmeg.text('');
				}else if(data.type == 2){
					errmeg.text('请您正确输入手机号码');
					return;
				}else if(data.type == 3){
					errmeg.text('您输入的手机号不存在');
					return;
				}
			}
		});
	});
	// 密码判断
	$('.logpass').change(function() {
		var pass = $.trim($(this).val());
		var errmeg = $(this).parent().find('.logerrmeg');
		if(pass.length < 6){
			errmeg.text('您输入的密码不能少于6位');
			return;
		}
		if(pass.length > 20){
			errmeg.text('您输入的密码不能超过20位');
			return;
		}
		errmeg.text('');
	});
	// 提交判断
	$('.logsub').click(function() {
		var _this = $(this);
		var mobile = $.trim($('.logmobile').val());
		var pass = $.trim($('.logpass').val());
		var mobileerr = $('.logmobile').parent().find('.logerrmeg');
		var passerr = $('.logpass').parent().find('.logerrmeg');
		if(mobileerr.text() != '') return;
		if(!mobile.match(/^1[34578]{1}\d{9}$/)){
			mobileerr.text('请您正确输入手机号码');
			return;
		}
		if(passerr.text() != '') return;
		if(pass.length < 6){
			passerr.text('您输入的密码不能少于6位');
			return;
		}
		if(pass.length > 20){
			passerr.text('您输入的密码不能超过20位');
			return;
		}
		$.ajax({
			url: _host + '/Login/getpas',
			type: 'post',
			dataType: 'json',
			data: {
				mobile: mobile,
				pass: pass
			},
			success: function(data){
				if(data.type == 1){
					$('form').submit();
				}else if(data.type == 2){
					mobileerr.text('请您正确输入手机号码');
					return;
				}else if(data.type == 3){
					passerr.text('您输入的密码不能少于6位');
					return;
				}else if(data.type == 4){
					passerr.text('您输入的密码不能超过20位');
					return;
				}else if(data.type == 5){
					passerr.text('您输入的手机和密码不匹配');
					return;
				}
			}
		});
	});

	/**
	 * 找回密码第一步
	 */
	$('.retimob').change(function() {
		var mobile = $(this).val();
		var errmeg = $(this).parent().find('.reterrmeg');
		if(!mobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.text('请您正确输入手机号码');
			return;
		}
		$.ajax({
			url: _host + '/Login/getmobile',
			type: 'post',
			dataType: 'json',
			data: {
				mobile: mobile
			},
			success: function(data){
				if(data.type == 1){
					errmeg.text('');
				}else if(data.type == 2){
					errmeg.text('请您正确输入手机号码');
					return;
				}else if(data.type == 3){
					errmeg.text('您输入的手机号不存在');
					return;
				}
			}
		});
	});

	// 验证图形验证码
	$('.retiimgcode').change(function() {
		var imgcode = $.trim($(this).val());
		var errmeg = $(this).parent().find('.reterrmeg');
		if(imgcode.length != 4){
			errmeg.text('请输入四位图形验证码');
			return;
		}
		$.ajax({
			url: _host + '/Retrieve/getimgcode',
			type: 'post',
			dataType: 'json',
			data: {
				imgcode: imgcode
			},
			success: function(data){
				if(data.type == 1){
					errmeg.text('');
				}else if(data.type == 2){
					errmeg.text('图形验证码不正确');
					return;
				}
			}
		});
	});
	// 提交数据
	$('.retisub').click(function() {
		var mobile = $.trim($('.retimob').val());
		var imgcode = $.trim($('.retiimgcode').val());
		var mobileerr = $('.retimob').parent().find('.reterrmeg');
		var imgcodeerr = $('.retiimgcode').parent().find('.reterrmeg');
		var errmeg = $(this).parent().find('.reterrmeg');
		if(!mobile.match(/^1[34578]{1}\d{9}$/)){
			mobileerr.text('请您正确输入手机号码');
			return;
		}
		if(mobileerr.text() != ''){
			// mobileerr.text('请您正确输入手机号码！');
			return;
		}
		if(imgcode.length != 4){
			imgcodeerr.text('请输入四位图形验证码');
			return;
		}
		if(imgcodeerr.text() != ''){
			// imgcodeerr.text('请输入正确图形验证码');
			return;
		}
		$('form').submit();
	});

	/**
	 * 找回密码第二步
	 */
	// 获取手机验证码
	$('.fdpassmeg').click(function() {
		var _this = $(this);
		var fdpassmob = $('.fdpassmob').text();
		var errmeg = $(this).parent().find('.reterrmeg');
		if(!fdpassmob.match(/^1[34578]{1}\d{9}$/)){
			errmeg.text('手机号码异常');
			return;
		}
		$.ajax({
			url: _host + '/Retrieve/getmeg',
			type: 'post',
			dataType: 'json',
			data: {
				meg: 'meg',
				fdpassmob: fdpassmob,
			},
			success: function(data){
				if(data.type == 1){
					_this.attr('disabled','disabled');
					_this.css({background: '#FFEEDD'});
					_this.html('<st>60</st>s后再次获取');
					var st = _this.find('st');
					var i = 59;
					var timer = setInterval(function(){
						if(i < 0) {
							_this.text('获取短信验证码');
							_this.css({background: 'white'});
							_this.removeAttr('disabled');
							clearInterval(timer);
						}else{
							st.text(i--);
						}
					},1000);
					return;
				}else if(data.type == 2){
					errmeg.text('获取异常，请稍后再试');
					return;
				}else if(data.type == 3){
					errmeg.text(data.error);
					return;
				}
			}
		});
	});
	// 验证手机验证码
	$('.retsmob').change(function() {
		var retsmob = $.trim($(this).val());
		var errmeg = $(this).parent().find('.reterrmeg');
		if(retsmob.length != 6){
			errmeg.text('请正确输入六位手机验证码');
			return;
		}
		$.ajax({
			url: _host + '/Register/getmegmeg',
			type: 'post',
			dataType: 'json',
			data: {
				mobcode: retsmob
			},
			success: function(data){
				if(data.type == 1){
					errmeg.text('');
				}else if(data.type == 2){
					errmeg.text('手机验证码已超时，请重新获取');
					return;
				}else if(data.type == 3){
					errmeg.text('手机验证码已超时，请重新获取');
					return;
				}else if(data.type == 4){
					errmeg.text('手机验证码不正确');
					return;
				}
			}
		});
	});
	// 提交验证
	$('.retssub').click(function() {
		var retsmob = $.trim($('.retsmob').val());
		var retsmoberr = $('.retsmob').parent().find('.reterrmeg');
		var errmeg = $(this).parent().find('.reterrmeg');
		if(retsmob.length != 6){
			retsmoberr.text('请正确输入六位手机验证码');
			return;
		}
		if(retsmoberr.text() != ''){
			// retsmoberr.text('请输入正确手机验证码');
			return;
		}
		$.ajax({
			url: _host + '/Register/getmegmeg',
			type: 'post',
			dataType: 'json',
			data: {
				mobcode: retsmob
			},
			success: function(data){
				if(data.type == 1){
					retsmoberr.text('');
					$('form').submit();
				}else if(data.type == 2){
					retsmoberr.text('手机验证码已超时，请重新获取');
					return;
				}else if(data.type == 3){
					retsmoberr.text('手机验证码已超时，请重新获取');
					return;
				}else if(data.type == 4){
					retsmoberr.text('手机验证码不正确');
					return;
				}
			}
		});
	});

	/**
	 * 找回密码第三步
	 */
	// 验证密码
	$('.rettpasd').change(function() {
		var rettpasd = $.trim($(this).val());
		var errmeg = $(this).parent().find('.reterrmeg');
		if(rettpasd == ''){
			errmeg.text('新密码不能为空');
			return;
		}
		if(rettpasd.length < 6){
			errmeg.text('6-20位大小写英文字母、符号或数字组合');
			return;
		}
		if(rettpasd.length > 20){
			errmeg.text('6-20位大小写英文字母、符号或数字组合');
			return;
		}
		$.ajax({
			url: _host + '/Retrieve/getpasd',
			type: 'post',
			dataType: 'json',
			data: {
				rettpasd: rettpasd
			},
			success: function(data){
				if(data.type == 1){
					errmeg.text('');
				}else if(data.type == 2){
					errmeg.text('用户信息不同步');
					return;
				}else if(data.type == 3){
					errmeg.text('新密码不能为空');
					return;
				}else if(data.type == 4){
					errmeg.text('用户信息异常');
					return;
				}else if(data.type == 5){
					errmeg.text('新密码不能与旧密码一致');
					return;
				}
			}
		});
	});
	// 确认密码
	$('.rettsupasd').change(function() {
		var rettpasd = $.trim($('.rettpasd').val());
		var rettsupasd = $.trim($(this).val());
		var errmeg = $(this).parent().find('.reterrmeg');
		if(rettsupasd == ''){
			rettsupasderr.text('确认密码不能为空');
			return;
		}
		if(rettpasd != rettsupasd){
			errmeg.text('新密码和确认新密码必须保持一致');
			return;
		}
		errmeg.text('');
	});
	// 提交
	$('.rettsub').click(function() {
		var rettpasd = $.trim($('.rettpasd').val());
		var rettsupasd = $.trim($('.rettsupasd').val());
		var rettpasderr = $('.rettpasd').parent().find('.reterrmeg');
		var rettsupasderr = $('.rettsupasd').parent().find('.reterrmeg');
		var errmeg = $(this).parent().find('.reterrmeg');
		if(rettpasderr.text() != ''){
			// rettpasderr.text('请正确填写新密码');
			return;
		}
		if(rettpasd == ''){
			rettpasderr.text('新密码不能为空');
			return;
		}
		if(rettsupasd == ''){
			rettsupasderr.text('确认密码不能为空');
			return;
		}
		if(rettsupasderr.text() != ''){
			// rettsupasderr.text('请正确填写确认新密码');
			return;
		}
		if(rettpasd != rettsupasd){
			rettsupasderr.text('新密码和确认密码不一致');
			return;
		}
		$('form').submit();
	});
	/**
	 * 提交需求定制
	 */
	// 手机号验证
	$('.xqmobile').change(function() {
		var xqmobile = $.trim($(this).val());
		var errmeg = $('.levitated');
		if(!xqmobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入手机号码');
			return;
		}
	});
	// 图形验证码
	$('.xqimgcode').change(function() {
		var _this = $(this);
		var xqimgcode = $.trim($(this).val());
		var errmeg = $('.levitated');
		if(xqimgcode.length != 4){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请输入四位图形验证码');
			return;
		}
		
	});
	// 手机验证码
	$('.xqmobcode').change(function(){
		var _this = $(this);
		var code = $(this).val();
		var errmeg = $('.levitated');
		var xqimgcname = $('.xqimgcode').attr('name');
		var xqmobile = $.trim($('.xqmobile').val());
		var xqimgcode = $.trim($('.xqimgcode').val());
		if(!xqmobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入手机号码');
			return;
		}
		$.ajax({
			url: _host + '/Custommade/checkmeg',
			type: 'POST',
			dataType: 'json',
			data: {
				code: code
			},
			success: function(data){
				if(data.type == 1){
					//$('.xqfj').show();
					_this.attr('name','mobcoder');
				}
				else if (data.type == 2) {
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码已超时，请重新获取102');
					return;
				}else if (data.type == 3) {
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码已超时，请重新获取103');
					return;
				}else if (data.type == 4) {
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码不正确');
					return;
				}
			}
		});
	});

	// 提交
	$('.main').on('click','.customsub',function() {
		var _this = $(this);
		var webcate = $('#wzjsd').find('dd').find('span').text();
		var zdfl = $('#zdfl-box').find('span').text();
		var app = $('#app-box').find('span').text();
		var yytg = $('#yytg-box').find('span').text();
		var wxkf = $('#wxkf-box').find('span').text();
		var fujian = $('#cftp').find('img').attr('value');
		var customtext = $('.customtext').val();
		var errmeg = $('.levitated');
		var xqimgcode = $.trim($('.xqimgcode').val());
		var xqimgcname = $('.xqimgcode').attr('name');
		var xqmobile = $.trim($('.xqmobile').val()); 
		var xqmobcode = $('.xqmobcode').val();
		var xqmobcodecname = $('.xqmobcode').attr('name');
		var xqimgs = $('#cftp').find('img');
		$('.xqwebcate').val(webcate);
		$('.xqclientcate').val(zdfl);
		$('.xqapp').val(app);
		$('.xqyunying').val(yytg);
		$('.xqweixin').val(wxkf);
		if(!xqmobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请输入正确手机号码');
			return;
		}
		if(customtext == ''){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请填写需求描述');
			return;
		}
		if(customtext != '' && customtext.length < 5){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('需求文字不能少于5个字符');
			return;
		} 
		$.ajax({
			url: _host + '/Custommade/checkmeg',
			type: 'POST',
			dataType: 'json',
			data: {
				code: xqmobcode, 
			},
			success: function(data){
				if(data.type == 1){
					$.ajax({
						url: _host + '/Custommade/writemeg',
						type: 'POST',
						dataType: 'json',
						data: {
							webcate: webcate,
							zdfl: zdfl,
							app: app,
							yytg: yytg,
							wxkf: wxkf,
							mobile: xqmobile,
							mobcoder: xqmobcode,
							customtext: customtext,
							fujian: fujian,
						},
						success: function(data){
							if(data.type == 1){
								$('#customModal').modal('show');
								setTimeout(function(){window.location.href = ''},2500);
							}else if(data.type == 2){
								errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入手机验证码');
								return;
							}else if(data.type == 3){
								errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码已超时，请重新获取！');
								return;
							}else if(data.type == 4){
								errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码已超时，请重新获取！');
								return;
							}else if(data.type == 5){
								errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码不正确！');
								return;
							}else if(data.type == 6){
								errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('提交信息失败，请稍后再试或联系管理员！');
								return;
							}
						}
					});
				}
				else if (data.type == 2) {
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码已超时，请重新获取102');
					return;
				}else if (data.type == 3) {
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码已超时，请重新获取103');
					return;
				}else if (data.type == 4) {
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('手机验证码不正确');
					return;
				}
			}
		});
		
	});

	/**
	 * [需求定制获取手机验证码]
	 * @param  {[type]} ) {		var       xqmobile [description]
	 * @return {[type]}   [description]
	 */
	$('.getcumeg').click(function() {
		var _this = $(this);
		var errmeg = $('.levitated');
		var xqmobile = $.trim($('.xqmobile').val());
		var xqimgcode = $.trim($('.xqimgcode').val());
		var xqimgcname = $('.xqimgcode').attr('name');
		if(!xqmobile.match(/^1[34578]{1}\d{9}$/)){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入手机号码');
			return;
		}
		if(xqimgcode.length != 4){
			errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('请正确输入四位图形验证码');
			return;
		}
		$.ajax({
			url: _host + '/Retrieve/getimgcode',
			type: 'post',
			dataType: 'json',
			data: {
				imgcode: xqimgcode
			},
			success: function(data){
				if(data.type == 1){
					$.ajax({
						url: _host + '/Custommade/getmeg',
						type: 'post',
						dataType: 'json',
						data: {
							meg: 'meg',
							xqmobile: xqmobile,
						},
						success: function(data){
							if(data.type == 1){
								_this.attr('disabled','disabled');
								_this.html('<st>60</st>s后再次获取');
								var st = _this.find('st');
								var i = 59;
								var timer = setInterval(function(){
									if(i < 0) {
										_this.text('获取短信验证码');
										_this.css({background: 'white'});
										_this.removeAttr('disabled');
										clearInterval(timer);
									}else{
										st.text(i--);
									}
								},1000);
								var src = $('.freshver').attr('src');
								$('.freshver').attr("src",chgUrl(src));
								return;
							}else if(data.type == 2){
								errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('获取异常，请稍后再试');
								return;
							}else if(data.type == 3){
								errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text(data.error);
								return;
							}
						}
					});
				}else if(data.type == 2){
					errmeg.fadeIn('slow',function(){setTimeout(function(){errmeg.fadeOut('slow')},2500)}).text('图形验证码不正确');
					return;
				}
			}
		});
	});
});