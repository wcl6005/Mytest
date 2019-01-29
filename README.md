一、python3.5 - django1.11.5 部署正常
二、功能：图片识别文字
三、应用：django微信小程序后台。
四、主要技术：
1、识别图像中的字符串，使用baidu-aip模块，优点是：快、准、简洁。
2、图像文件上传，选择文件后直接自动提交。
3、django程序运行，前台有动画的图标
4、前台实现文件内容的拷贝、粘贴。
5、后台实现上传文件大小设定：支持识别的文件大小,不得大于8MB。
6、在线生成条形码、二维码。

五、存在问题
1、批量生成条形码，输入框第二行内容也预览了。正确：应该只预览第一行内容。
2、QR_code.html中，qrcode16.js文件，在线使用和下载到本地使用，对浏览器Firefox支持有影响
<script src="https://static.gaitubao.net/js/qrcode16.js"></script> 不支持浏览器：Firefox 
<script src="/static/prettify/js/qrcode16.js"></script>   不知为什么？