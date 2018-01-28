/*设置Qiniu.uploader对象参数*/  
function getOption(button, product_id){
    return {  
        runtimes: 'html5,flash,html4',    //上传模式,依次退化  
        // container: imageContainer,           //上传区域DOM ID，默认是browser_button的父元素，  
        // drop_element: imageContainer,        //拖曳上传区域元素的ID，拖曳文件或文件夹后可触发上传  
        browse_button: button,       //上传选择的点选按钮，**必需**  
        uptoken_url: $('#uptoken_url').val(),            //Ajax请求upToken的Url，**强烈建议设置**（服务端提供）
//        uptoken : token, //若未指定uptoken_url,则必须指定 uptoken ,uptoken由其他程序生成
        // save_key: true,   // 默认 false。若在服务端生成uptoken的上传策略中指定了 `sava_key`，则开启，SDK会忽略对key的处理  
        domain: 'http://p1tbqu4i5.bkt.clouddn.com/',   //bucket 域名，下载资源时用到，**必需**
        get_new_uptoken: false,  //设置上传文件的时候是否每次都重新获取新的token  
        max_file_size: '10mb',           //最大文件体积限制  
        flash_swf_url: 'plupload/Moxie.swf',  //引入flash,相 对路径
        max_retries: 3,                   //上传失败最大重试次数  
        dragdrop: true,                   //开启可拖曳上传  
        chunk_size: '10mb',                //分块上传时，每片的体积  
        auto_start: false,                 //选择文件后自动上传，若关闭需要自己绑定事件触发上传  
        unique_names: true,      //设置所有文件名唯一  
        filters: {  
            mime_types : [ //只允许上传图片  
                { title : "Image files", extensions : "jpg,jpeg,gif,png" },  
            ],  
            prevent_duplicates : false //不允许选取重复文件  
        },  
        deleteAfterDays:'',  
        init: {  
            'FilesAdded': function(up, files) {//up:队列, 
              console.log(up.files.length);
              plupload.each(files, function(file) {
                var tag_file=$("<div></div>");
                tag_file.text(file.name);
                $("#div_content_contaner").append(tag_file);
              });
                // // 设置预览图地址  
              // var tag_img=$("<img></img>");
              //   // tag_img.attr("src", img_url);
              // tag_img.attr("class", "image_product_content");
              //   // var id_img = 'img_content'+arrContents.length;
              //   // tag_img.attr("id", id_img);
              // $("#div_content_contaner").append(tag_img);
              
                // img.load(files[0].getSource());  
                // // 开始上传按钮  
                // $("#" + button + "_start").click(function(){ up.start(); });  
                // plupload.each(files, function(file) {  
                //     // 如果上传文件大于1 ps：第一个文件上传的时候用户选择第二个文件  
                //     // 这时队列大于1，队列的第一个文件是正在上传的，第二个是新选的  
                //     if (up.files.length > 1) {  
                //         // 移除当前队列里第一个文件  
                //         up.removeFile(up.files[0]);  
                //     }  
                //     // 全局变量 根据变量控制不让表单提前提交  
                //     imgloading = true;  
                //     // 文件添加进队列后,处理相关的事情  
                // });  
            },  
            'BeforeUpload': function(up, file) {  
                // 每个文件上传前,处理相关的事情  
                // $("#" + button + "_uploading").click(function () {  
                //     up.stop();  
                //     $("#" + button + "_uploading").fadeOut();  
                // });  
            },  
            'UploadProgress': function(up, file) {  
                // if($("#" + button + "_uploading").length < 1){  
                //     return;  
                // }  
                // $("#" + button + "_uploading").show();  
                // $("#" + button + "_uploading").html(up.total.percent + "%（点击取消）");  
                   // 每个文件上传时,处理相关的事情  
            },  
            'FileUploaded': function(up, file, info) {  
                var res = $.parseJSON(info.response);  
                console.log(res.key);
                arrImgName.push(res.key);
                // // 设置图片名称  
                // $("#" + button + "_input").val(res.key);  
                // // 进度更新为上传完成  
                // $("#" + button + "_uploading").html("上传完成");  
                // $("#" + button + "_uploading").unbind();  
                // 图片上传后执行事件  
                // eval(last+"()");  
                // last();  
            },  
            'Error': function(up, err, errTip) {  
                // alert("目前只支持图片格式：jpg,jpeg,gif,png");  
                   //上传出错时,处理相关的事情  
            },  
            'UploadComplete': function() {  
                   //队列文件处理完毕后,处理相关的事情  
              console.log(arrImgName);
              postContent(product_id);
            }
        }  
    };  
}

$.ajaxSetup({  
  beforeSend: function(xhr, settings){   
      var csrftoken = $.cookie('csrftoken');   
      xhr.setRequestHeader("X-CSRFToken", csrftoken);   
  }  
});

function postContent(product_id){
  var children = $('#div_content_contaner').children();
  var imgIndex = 0;
  for (var i = 0; i < children.length; i++) {
    if (children[i].tagName == 'DIV') {
      arrContents.push(arrImgName[imgIndex]);
      imgIndex++;
    } else {
      arrContents.push(children[i].value);
    }
  }
  var contentJsonArr = JSON.stringify(arrContents);
  console.log(contentJsonArr);
  $.post('/util/products/edit_content/',{
    'id':product_id,
    'contents':contentJsonArr,
    'X-CSRFToken': $.cookie('csrftoken'),
  }, function(data,status){
    alert(status)
  });
}