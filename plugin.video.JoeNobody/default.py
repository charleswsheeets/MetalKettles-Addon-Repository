import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os
import plugintools

AddonID ='plugin.video.JoeNobody'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))

def Index():
    plugintools.add_item( 
        title="JoeNobody 010101",
        url="plugin://plugin.video.youtube/user/JoeNobody010101/",
        thumbnail=icon,
        folder=True,
        fanart=xbmc.translatePath(os.path.join('special://home/addons/' + AddonID , 'fanart.jpg')))       

def PlayStream(url,iconimage):
    playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
    ok=True
    xbmc.Player ().play(playback_url)
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

params=get_params();url=None;name=None;mode=None;iconimage=None;description=None
try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:iconimage=urllib.unquote_plus(params["iconimage"])
except:pass
try:mode=int(params["mode"])
except:pass
try:description=urllib.unquote_plus(params["description"])
except:pass

print "Mode: "+str(mode);print "URL: "+str(url);print "Name: "+str(name);print "IconImage: "+str(iconimage)
   
if mode==None or url==None or len(url)<1:Index()
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
