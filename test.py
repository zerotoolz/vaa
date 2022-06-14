import agorartc 
rtc = agorartc.createRtcEngineBridge()
eventHandler = agorartc.RtcEngineEventHandlerBase()
rtc.initEventHandler(eventHandler)
0 (Success)
rtc.initialize("f3d54112e0b243599ff58abcbd4ed38c", None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)  # If you do not have an App ID, see Appendix (https://github.com/AgoraIO-Community/Agora-Python-SDK#appendix).
0 (Success)
rtc.enableVideo()
0 (Success)
rtc.joinChannel("", "channel-name", "", 0)
0 (Success)
rtc.leaveChannel()  # Leave channel
0 (Success)
rtc.release()