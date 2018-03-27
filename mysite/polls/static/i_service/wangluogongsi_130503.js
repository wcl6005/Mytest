if (1 == 1) {
    document.write(" <style> ")
    document.write(".div_voide")
    document.write("{")
    document.write("position: fixed;")
    document.write("_position:absolute;")
    document.write("bottom:0px;")
    document.write("width: 300px;")
    document.write("height: 400px; ")
    document.write(" z-index:999;")
    document.write("right:0px; ")
    document.write("background-color: Transparent;")
    document.write("}")
    document.write("</style>")
    document.write("<div onmousedown='cc1.create(this)' id='video' class='div_voide' >");
    document.write("<div Style='position: absolute; bottom:0px; right:0px; z-index:999;'>");
    document.write("<a href=\"JavaScript:;\" onclick=\"hidead()\" style=\"color:Red;text-decoration:none;font-size:12px;\">关闭</a>");
    document.write("</div>");
    document.write("<object classid='clsid:D27CDB6E-AE6D-11cf-96B8-444553540000' codebase='http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0'");
    document.write("width='300' height='400' id='FLVPlayer'>");
    document.write("<param name='wmode' value='transparent'>");
    document.write("<param name='movie' value='http://www.web0512.net/FLVPlayer_Progressive.swf' />");
    document.write("<param name='salign' value='lt' />");
    document.write("<param name='quality' value='high' />");
    document.write("<param name='scale' value='noscale' />");
    document.write("<param name='FlashVars' value='&MM_ComponentVersion=1&skinName=http://www.web0512.net/Clear_Skin_1&streamName=http://www.web0512.net/wangluogongsi_130503&autoPlay=true&autoRewind=false' />");
    document.write("<embed wmode='transparent' src='http://www.web0512.net/FLVPlayer_Progressive.swf' flashvars='&MM_ComponentVersion=1&skinName=http://www.web0512.net/Clear_Skin_1&streamName=http://www.web0512.net/wangluogongsi_130503&autoPlay=true&autoRewind=false'");
    document.write("quality='high' scale='noscale' width='300' height='400' name='FLVPlayer' salign='LT'");
    document.write("type='application/x-shockwave-flash' pluginspage='http://www.macromedia.com/go/getflashplayer' />");
    document.write("</object>");
    document.write("</div>");
    function hidead() {
        var my = document.getElementById("video");
        if (my != null)
            my.parentNode.removeChild(my);
    }
    var browser = navigator.appName;
    var b_version = navigator.appVersion;
    var version = b_version.split(";");
    var trim_Version = version[1].replace(/[ ]/g, ""); if (browser == "Microsoft Internet Explorer" && trim_Version == "MSIE6.0") {
        function rightBottomAd() {
            var abc = document.getElementById("video");
            abc.style.top = document.documentElement.scrollTop + document.documentElement.clientHeight - 400 + "px";
            setTimeout(function () { rightBottomAd(); }, 50);
        }
        rightBottomAd();
    }
    else
    { }
    }
     else {
    document.write(" <style> ")
    document.write(".div_voide")
    document.write("{")
    document.write("position: fixed;")
    document.write("_position:absolute;")
    document.write("bottom:0px;")
    document.write("width: 300px;")
    document.write("height: 400px; ")
    document.write(" z-index:999;")
    document.write("right:0px; ")
    document.write("background-color: Transparent;")
    document.write("}")
    document.write("</style>")
    document.write("<div onmousedown='cc1.create(this)' id='video' class='div_voide' style='background-color: black;' >");
    alert("您盗用了视频");
    document.write("</div>");
}
