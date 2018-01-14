from qiniu import Auth, put_file, etag
from django.conf import settings

class Helpers:

    @classmethod
    def upload_file(cls, file, cloud_file_name):
        # 构建鉴权对象
        q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        # 上传到七牛后保存的文件名
        key = cloud_file_name
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(settings.QINIU_BUCKET_NAME, key, 3600)
        # 保存临时文件
        file_path = 'static/temp.jpg'
        destination = open(file_path, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        # 要上传文件的本地路径
        local_file = file_path
        ret, info = put_file(token, key, local_file)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(local_file)

    @classmethod
    def get_cloud_file_url(cls, cloud_file_name):
        q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        # 有两种方式构造base_url的形式
        base_url = '%s%s' % (settings.QINIU_DOMAIN, cloud_file_name)
        # 可以设置token过期时间
        private_url = q.private_download_url(base_url, expires=3600)
        print(private_url)
        # r = requests.get(private_url)
        # assert r.status_code == 200
        return private_url
