from bs4 import BeautifulSoup as BS
from .weapons import get_logger

log = get_logger('weixin')

def parse_message_body(message_body=None):
    if not message_body:
        return None
    rst = {}
    try:
        xml = BS(message_body, 'xml')
        if xml.Encrypt:
            rst['Encrypt'] = xml.Encrypt.text
        if xml.URL:
            rst['URL'] = xml.URL.text
        if xml.ToUserName:
            rst['ToUserName'] = xml.ToUserName.text
        if xml.FromuserName:
            rst['FromUserName'] = xml.FromUserName.text
        if xml.CreateTime:
            rst['CreateTime'] = int(xml.CreateTime.text)
        if xml.MsgType:
            rst['MsgType'] = xml.MsgType.text
        if xml.Content:
            rst['Content'] = xml.Content.text
        if xml.MsgId:
            rst['MsgId'] = int(xml.MsgId.text)
        if xml.PicUrl:
            rst['PicUrl'] = xml.PicUrl.text
        if xml.MediaId:
            rst['MediaId'] = xml.MediaId.text
        if xml.Format:
            rst['Format'] = xml.Format.text
        if xml.ThumbMediaId:
            rst['ThumbMediaId'] = xml.ThumbMediaId.text
        if xml.Location_X:
            rst['Location_X'] = xml.Location_X.text
        if xml.Location_Y:
            rst['Location_Y'] = xml.Location_Y.text
        if xml.Scale:
            rst['Scale'] = xml.Scale.text
        if xml.Label:
            rst['Label'] = xml.Label.text
        if xml.Title:
            rst['Title'] = xml.Title.text
        if xml.Description:
            rst['Description'] = xml.Description.text
        if xml.Url:
            rst['Url'] = xml.Url.text
    except Exception as e:
        log.error(e)
        return None
    return rst


def reply_text_message(to_user, from_user, content):
    msg = """
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>12345678</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>
    """ % (to_user, from_user, content)
    return msg

