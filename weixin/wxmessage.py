from bs4 import BeautifulSoup as BS
from .config import wx_token, wx_aeskey, appid
from .weapons import get_logger
from .wxcrypt import WXBizMsgCrypt
from weixin import ierror

log = get_logger()


def parse_message_body(message_body=None):
    if not message_body:
        return {}
    rst = {}
    try:
        xml = BS(message_body, 'xml')
        if xml.Encrypt:
            rst['Encrypt'] = xml.Encrypt.text
        if xml.URL:
            rst['URL'] = xml.URL.text
        if xml.ToUserName:
            rst['ToUserName'] = xml.ToUserName.text
        if xml.FromUserName:
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
        if xml.Event:
            rst['Event'] = xml.Event.text
    except Exception as e:
        log.error(e)
        return {}
    return rst


def text_message(to_user, from_user, create_time, content):
    msg = """
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>
    """ % (to_user, from_user, create_time, content)
    log.info(msg)
    log.info('msg type %s', type(msg))
    return msg


def decrypted_message_body(sPostData, sMsgSignature, sTimeStamp, sNonce):
    """
    :param sPostData:
    :param sMsgSignature:
    :param sTimeStamp:
    :param sNonce:
    :return: parse_message_body parsed args
    """
    msg_crypt = WXBizMsgCrypt(wx_token, wx_aeskey, appid)
    ret, xml_body = msg_crypt.DecryptMsg(sPostData, sMsgSignature, sTimeStamp, sNonce)
    if ret == ierror.WXBizMsgCrypt_OK:
        return parse_message_body(xml_body)
    return None


def encrypted_message_body(sReplyMsg, sNonce, timestamp=None):

    msg_crypt = WXBizMsgCrypt(wx_token, wx_aeskey, appid)
    ret, xml_body = msg_crypt.EncryptMsg(sReplyMsg, sNonce, timestamp)
    if ret == ierror.WXBizMsgCrypt_OK:
        return xml_body
    return ''
