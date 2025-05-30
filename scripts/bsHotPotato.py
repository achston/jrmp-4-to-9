import bs
import random 
def bsGetAPIVersion ():
    return 4 
def bsGetGames ():
    return [HotPotatoGame ]
class Icon (bs .Actor ):
    def __init__ (O0O000OO0OO00000O ,OO0OOOO00O00O00O0 ,O0OO0OOOO000O0000 ,OOOOOO0O0O0O00OOO ,nameScale =1.0 ,nameMaxWidth =115.0 ,shadow =1.0 ):
        bs .Actor .__init__ (O0O000OO0OO00000O )
        O0O000OO0OO00000O ._player =OO0OOOO00O00O00O0 
        O0O000OO0OO00000O ._nameScale =nameScale 
        O0O000OO0OO00000O ._outlineTex =bs .getTexture ('characterIconMask')
        O000O0OOO00O00OOO =OO0OOOO00O00O00O0 .getIcon ()
        O0O000OO0OO00000O .node =bs .newNode ('image',owner =O0O000OO0OO00000O ,attrs ={'texture':O000O0OOO00O00OOO ['texture'],'tintTexture':O000O0OOO00O00OOO ['tintTexture'],'tintColor':O000O0OOO00O00OOO ['tintColor'],'vrDepth':400 ,'tint2Color':O000O0OOO00O00OOO ['tint2Color'],'maskTexture':O0O000OO0OO00000O ._outlineTex ,'opacity':1.0 ,'absoluteScale':True ,'attach':'bottomCenter'})
        O0O000OO0OO00000O ._nameText =bs .newNode ('text',owner =O0O000OO0OO00000O .node ,attrs ={'text':OO0OOOO00O00O00O0 .getName (),'color':bs .getSafeColor (OO0OOOO00O00O00O0 .getTeam ().color ),'hAlign':'center','vAlign':'center','vrDepth':410 ,'maxWidth':nameMaxWidth ,'shadow':shadow ,'flatness':1.0 ,'hAttach':'center','vAttach':'bottom'})
        O0O000OO0OO00000O ._infectText =bs .newNode ('text',owner =O0O000OO0OO00000O .node ,attrs ={'text':'Marked!','color':(1 ,0.1 ,0.0 ),'hAlign':'center','vrDepth':430 ,'shadow':1.0 ,'flatness':1.0 ,'hAttach':'center','vAttach':'bottom'})
        O0O000OO0OO00000O .setPositionAndScale (O0OO0OOOO000O0000 ,OOOOOO0O0O0O00OOO )
    def setPositionAndScale (OO0O0OOOOOO0O00OO ,O0O00O0OOO0OOO00O ,OOOOOO0OO0OOOOOO0 ):
        OO0O0OOOOOO0O00OO .node .position =O0O00O0OOO0OOO00O 
        OO0O0OOOOOO0O00OO .node .scale =[70.0 *OOOOOO0OO0OOOOOO0 ]
        OO0O0OOOOOO0O00OO ._nameText .position =(O0O00O0OOO0OOO00O [0 ],O0O00O0OOO0OOO00O [1 ]+OOOOOO0OO0OOOOOO0 *52.0 )
        OO0O0OOOOOO0O00OO ._nameText .scale =1.0 *OOOOOO0OO0OOOOOO0 *OO0O0OOOOOO0O00OO ._nameScale 
        OO0O0OOOOOO0O00OO ._infectText .position =(O0O00O0OOO0OOO00O [0 ],O0O00O0OOO0OOO00O [1 ]-OOOOOO0OO0OOOOOO0 *52.0 )
        OO0O0OOOOOO0O00OO ._infectText .scale =1.0 *OOOOOO0OO0OOOOOO0 
    def updateForInfection (OO0O00O0OO00OO000 ):
        if OO0O00O0OO00OO000 ._player .exists ():
            O0OOO00O00O00OOOO =OO0O00O0OO00OO000 ._player .gameData ['infected']
            OO00OOO0O00O00000 =OO0O00O0OO00OO000 ._player .gameData ['eliminated']
        if O0OOO00O00O00OOOO :
            OO0O00O0OO00OO000 ._infectText .text ='Marked!'
            OO0O00O0OO00OO000 ._nameText .flatness =0.0 
            OO0O00O0OO00OO000 .node .color =(1.0 ,0.7 ,0.7 )
        else :
            OO0O00O0OO00OO000 ._infectText .text =''
            OO0O00O0OO00OO000 ._nameText .flatness =1.0 
            OO0O00O0OO00OO000 .node .color =(1.0 ,1.0 ,1.0 )
        if OO00OOO0O00O00000 :
            OO0O00O0OO00OO000 ._nameText .opacity =0.2 
            OO0O00O0OO00OO000 .node .color =(0.7 ,0.3 ,0.3 )
            OO0O00O0OO00OO000 .node .opacity =0.2 
    def handlePlayerSpawned (O0000O0OOOO00OO0O ):
        if not O0000O0OOOO00OO0O .node .exists ():return 
        O0000O0OOOO00OO0O .node .opacity =1.0 
    def handlePlayerDied (O0OO00O0OO0O0OO00 ):
        if not O0OO00O0OO0O0OO00 .node .exists ():return 
        O0OO00O0OO0O0OO00 ._infectText .text ='TIME OUT!'
        bs .animate (O0OO00O0OO0O0OO00 ._infectText ,'opacity',{0 :1.0 ,1000 :0.0 })
        bs .animate (O0OO00O0OO0O0OO00 .node ,'opacity',{0 :1.0 ,50 :0.0 ,100 :1.0 ,150 :0.0 ,200 :1.0 ,250 :0.0 ,300 :1.0 ,350 :0.0 ,400 :1.0 ,450 :0.0 ,500 :1.0 ,550 :0.2 })
class PotatoPlayerSpaz (bs .PlayerSpaz ):
    def __init__ (OO00O00O0000O00OO ,*O00OO0O0O0000OOO0 ,**OO0OO00OO0O0O0O0O ):
        super (OO00O00O0000O00OO .__class__ ,OO00O00O0000O00OO ).__init__ (*O00OO0O0O0000OOO0 ,**OO0OO00OO0O0O0O0O )
        OO00O00O0000O00OO .infectionLight =bs .newNode ('light',owner =OO00O00O0000O00OO .node ,attrs ={'position':OO00O00O0000O00OO .node .position ,'radius':0.15 ,'intensity':0.0 ,'heightAttenuated':False ,'color':(1.0 ,0.0 ,0.0 )})
        bs .animate (OO00O00O0000O00OO .infectionLight ,'radius',{0 :0.1 ,300 :0.15 ,600 :0.1 },loop =True )
        OO00O00O0000O00OO .node .connectAttr ('positionCenter',OO00O00O0000O00OO .infectionLight ,'position')
        OO00O00O0000O00OO .infectionTimerOffset =bs .newNode ('math',owner =OO00O00O0000O00OO .node ,attrs ={'input1':(0 ,1.2 ,0 ),'operation':'add'})
        OO00O00O0000O00OO .node .connectAttr ('torsoPosition',OO00O00O0000O00OO .infectionTimerOffset ,'input2')
        OO00O00O0000O00OO .infectionTimerText =bs .newNode ('text',owner =OO00O00O0000O00OO .node ,attrs ={'text':"999",'inWorld':True ,'shadow':0.4 ,'color':(1.0 ,0.2 ,0.2 ,0.0 ),'flatness':0 ,'scale':0.02 ,'hAlign':'center'})
        OO00O00O0000O00OO .infectionTimerOffset .connectAttr ('output',OO00O00O0000O00OO .infectionTimerText ,'position')
    def handleMessage (O0OOO0O0O0000O000 ,O000O0OOO00OO000O ):
        if isinstance (O000O0OOO00OO000O ,bs .HitMessage ):
            if not O0OOO0O0O0000O000 .node .exists ():
                return 
            if O000O0OOO00OO000O .sourcePlayer in bs .getActivity ().players and O000O0OOO00OO000O .sourcePlayer .gameData ['infected']:
                if O0OOO0O0O0000O000 .sourcePlayer ==O000O0OOO00OO000O .sourcePlayer :pass 
                else :
                    bs .getActivity ().infect (O0OOO0O0O0000O000 .sourcePlayer )
                    bs .getActivity ().infectRemove (O000O0OOO00OO000O .sourcePlayer )
            O0OOOOO0000OOOO00 =bs .getGameTime ()
            if O0OOO0O0O0000O000 ._lastHitTime is None or O0OOOOO0000OOOO00 -O0OOO0O0O0000O000 ._lastHitTime >1000 :
                O0OOO0O0O0000O000 ._numTimesHit +=1 
                O0OOO0O0O0000O000 ._lastHitTime =O0OOOOO0000OOOO00 
            O0000O0O0OO0O0OOO =O000O0OOO00OO000O .magnitude *O0OOO0O0O0000O000 ._impactScale 
            OOO000OO0O0OOO000 =O000O0OOO00OO000O .velocityMagnitude *O0OOO0O0O0000O000 ._impactScale 
            O000O0O000000O0OO =0.22 
            if O000O0OOO00OO000O .flatDamage :
                OOOO0OOO0OOOOOOO0 =O000O0OOO00OO000O .flatDamage *O0OOO0O0O0000O000 ._impactScale 
            else :
                O0OOO0O0O0000O000 .node .handleMessage ("impulse",O000O0OOO00OO000O .pos [0 ],O000O0OOO00OO000O .pos [1 ],O000O0OOO00OO000O .pos [2 ],O000O0OOO00OO000O .velocity [0 ],O000O0OOO00OO000O .velocity [1 ],O000O0OOO00OO000O .velocity [2 ],O0000O0O0OO0O0OOO ,OOO000OO0O0OOO000 ,O000O0OOO00OO000O .radius ,0 ,O000O0OOO00OO000O .forceDirection [0 ],O000O0OOO00OO000O .forceDirection [1 ],O000O0OOO00OO000O .forceDirection [2 ])
                OOOO0OOO0OOOOOOO0 =O000O0O000000O0OO *O0OOO0O0O0000O000 .node .damage 
                O0OOO0O0O0000O000 .node .handleMessage ("hurtSound")
            if O000O0OOO00OO000O .hitType =='punch':
                O0OOO0O0O0000O000 .onPunched (OOOO0OOO0OOOOOOO0 )
                if OOOO0OOO0OOOOOOO0 >500 :
                    O0OOOOOO0000O00O0 =O0OOO0O0O0000O000 .getFactory ().punchSoundsStrong 
                    OO0O0O000O0O000OO =O0OOOOOO0000O00O0 [random .randrange (len (O0OOOOOO0000O00O0 ))]
                else :OO0O0O000O0O000OO =O0OOO0O0O0000O000 .getFactory ().punchSound 
                bs .playSound (OO0O0O000O0O000OO ,1.0 ,position =O0OOO0O0O0000O000 .node .position )
                bs .emitBGDynamics (position =O000O0OOO00OO000O .pos ,velocity =(O000O0OOO00OO000O .forceDirection [0 ]*0.5 ,O000O0OOO00OO000O .forceDirection [1 ]*0.5 ,O000O0OOO00OO000O .forceDirection [2 ]*0.5 ),count =min (10 ,1 +int (OOOO0OOO0OOOOOOO0 *0.0025 )),scale =0.3 ,spread =0.03 )
                bs .emitBGDynamics (position =O000O0OOO00OO000O .pos ,chunkType ='sweat',velocity =(O000O0OOO00OO000O .forceDirection [0 ]*1.3 ,O000O0OOO00OO000O .forceDirection [1 ]*1.3 +5.0 ,O000O0OOO00OO000O .forceDirection [2 ]*1.3 ),count =min (30 ,1 +int (OOOO0OOO0OOOOOOO0 *0.04 )),scale =0.9 ,spread =0.28 )
                O0OO00OOOO0O000OO =OOOO0OOO0OOOOOOO0 *0.003 
                O0OO00OOOO0O000OO =min (O0OO00OOOO0O000OO ,750 *0.003 )
                O000OOOO00OO0O000 =(O000O0OOO00OO000O .pos [0 ]+O000O0OOO00OO000O .forceDirection [0 ]*0.02 ,O000O0OOO00OO000O .pos [1 ]+O000O0OOO00OO000O .forceDirection [1 ]*0.02 ,O000O0OOO00OO000O .pos [2 ]+O000O0OOO00OO000O .forceDirection [2 ]*0.02 )
                O00O000OOO00O0O00 =(1.0 ,0.8 ,0.4 )
                OOO00000O000OO0O0 =bs .newNode ("light",attrs ={'position':O000OOOO00OO0O000 ,'radius':0.12 +O0OO00OOOO0O000OO *0.12 ,'intensity':0.3 *(1.0 +1.0 *O0OO00OOOO0O000OO ),'heightAttenuated':False ,'color':O00O000OOO00O0O00 })
                bs .gameTimer (60 ,OOO00000O000OO0O0 .delete )
                O0O00O0OOOO00OOOO =bs .newNode ("flash",attrs ={'position':O000OOOO00OO0O000 ,'size':0.17 +0.17 *O0OO00OOOO0O000OO ,'color':O00O000OOO00O0O00 })
                bs .gameTimer (60 ,O0O00O0OOOO00OOOO .delete )
            if O000O0OOO00OO000O .hitType =='impact':
                bs .emitBGDynamics (position =O000O0OOO00OO000O .pos ,velocity =(O000O0OOO00OO000O .forceDirection [0 ]*2.0 ,O000O0OOO00OO000O .forceDirection [1 ]*2.0 ,O000O0OOO00OO000O .forceDirection [2 ]*2.0 ),count =min (10 ,1 +int (OOOO0OOO0OOOOOOO0 *0.01 )),scale =0.4 ,spread =0.1 )
        else :super (O0OOO0O0O0000O000 .__class__ ,O0OOO0O0O0000O000 ).handleMessage (O000O0OOO00OO000O )
class HotPotatoGame (bs .TeamGameActivity ):
    @classmethod 
    def getName (OO00O000OO00O0OO0 ):
        return 'Hot Potato'
    @classmethod 
    def getDescription (OOOOOOOOOOOOO000O ,OO00O000O0O00O00O ):
        return 'A random player gets marked.\nPass the mark to other players.\nMarked player gets eliminated when time runs out.\nLast one standing wins!'
    def getInstanceDescription (O000OO0O00O0O0OOO ):
        return 'Pass the mark to someone else before you explode!'
    @classmethod 
    def supportsSessionType (OOO00O0OOO00O0O0O ,O0O0000O0O0O0OO0O ):
        return True if issubclass (O0O0000O0O0O0OO0O ,bs .FreeForAllSession )else False 
    @classmethod 
    def getSupportedMaps (O0OO00O0O0OOO0OOO ,OOO0OO0000O0OOOOO ):
        return bs .getMapsSupportingPlayType ("melee")
    @classmethod 
    def getScoreInfo (OO00OOO0O000OO00O ):
        return {'scoreName':'Survived'}
    @classmethod 
    def getSettings (O0OO0O00O0OO000O0 ,O000O0O00OOOO00OO ):
        return [("Elimination Timer",{'minValue':1 ,'default':15 ,'increment':1 }),('Epic Mode',{'default':False })]
    def __init__ (OO000000O0O0O0OO0 ,OO00O0O000000O0OO ):
        bs .TeamGameActivity .__init__ (OO000000O0O0O0OO0 ,OO00O0O000000O0OO )
        if OO000000O0O0O0OO0 .settings ['Epic Mode']:OO000000O0O0O0OO0 ._isSlowMotion =True 
        OO000000O0O0O0OO0 ._tickSound =bs .getSound ('tick')
        OO000000O0O0O0OO0 ._dangerTickSound =bs .getSound ('punchStamina')
        OO000000O0O0O0OO0 ._infectedSound =bs .getSound ('nightmareSpecialWave')
        OO000000O0O0O0OO0 ._playerEliminatedSound =bs .getSound ('playerDeath')
    def onTransitionIn (OOOOOOO0O0OOO0OOO ):
        bs .TeamGameActivity .onTransitionIn (OOOOOOO0O0OOO0OOO ,music ='Epic'if OOOOOOO0O0OOO0OOO .settings ['Epic Mode']else 'Where Eagles Dare')
    def onBegin (O0O00000OOOO00000 ):
        bs .TeamGameActivity .onBegin (O0O00000OOOO00000 )
        O0O00000OOOO00000 .setupStandardPowerupDrops (enablePowerups =False ,enableTNT =False ,enableHazards =True )
        O0O00000OOOO00000 ._eliminationTimer =None 
        O0O00000OOOO00000 .eliminationTimerDisplay =0 
        if len (O0O00000OOOO00000 .players )<2 :
            O0O00000OOOO00000 .players [0 ].getTeam ().gameData ['survivor']=True 
            O0O00000OOOO00000 ._endGameTimer =bs .Timer (1250 ,bs .WeakCall (O0O00000OOOO00000 .endGame ))
        else :
            def O00OO000O0OO00OOO ():
                if len (O0O00000OOOO00000 .players )<=1 :
                    O0O00000OOOO00000 .endGame ()
                    return 
                else :O0O00000OOOO00000 .infect (random .choice (O0O00000OOOO00000 .getAlivePlayers ()),False )
            O0O00000OOOO00000 ._infectTimer =bs .Timer (2000 if O0O00000OOOO00000 ._isSlowMotion else 4400 ,O00OO000O0OO00OOO )
        O0O00000OOOO00000 ._updateIcons ()
    def onPlayerJoin (O0OOOO0O0O00OO00O ,O0O000O0OO000OOOO ):
        O0O000O0OO000OOOO .gameData ['infected']=False 
        O0O000O0OO000OOOO .getTeam ().gameData ['survivor']=False 
        O0O000O0OO000OOOO .gameData ['fallTimes']=0 
        if O0OOOO0O0O00OO00O .hasBegun ():
            O0O000O0OO000OOOO .gameData ['eliminated']=True 
            O0O000O0OO000OOOO .gameData ['icons']=[]
            bs .screenMessage (bs .Lstr (resource ='playerDelayedJoinText',subs =[('${PLAYER}',O0O000O0OO000OOOO .getName (full =True ))]),color =(0 ,1 ,0 ))
            return 
        O0O000O0OO000OOOO .gameData ['eliminated']=False 
        O0O000O0OO000OOOO .gameData ['icons']=[Icon (O0O000O0OO000OOOO ,position =(0 ,50 ),scale =0.8 )]
        O0OOOO0O0O00OO00O .spawnPlayer (O0O000O0OO000OOOO )
        if O0OOOO0O0O00OO00O .hasBegun ():
            O0OOOO0O0O00OO00O ._updateIcons ()
    def _updateIcons (O0OO000OOOO00O0OO ):
        O0O000OOO00OOO00O =len (O0OO000OOOO00O0OO .teams )
        OO000OOO0000OO0OO =100 
        OOOOOO0O0OOO0O00O =OO000OOO0000OO0OO *(O0O000OOO00OOO00O -1 )*-0.5 
        for O0000O000O0O0OOO0 ,OOO00OO0O0O0O00O0 in enumerate (O0OO000OOOO00O0OO .teams ):
            OOO0OOOO0O0000OOO =OOO00OO0O0O0O00O0 .players [0 ]
            for O000OO0OOOOO00OOO in OOO0OOOO0O0000OOO .gameData ['icons']:
                O000OO0OOOOO00OOO .setPositionAndScale ((OOOOOO0O0OOO0O00O ,50 ),0.8 )
                O000OO0OOOOO00OOO .updateForInfection ()
            OOOOOO0O0OOO0O00O +=OO000OOO0000OO0OO 
    def infect (O0000O00O00O0OO00 ,OO000000O0O000OOO ,passing =True ):
        OO000000O0O000OOO .gameData ['infected']=True 
        OO000000O0O000OOO .actor .infectionLight .intensity =1.5 
        OO000000O0O000OOO .actor .infectionTimerText .color =(OO000000O0O000OOO .actor .infectionTimerText .color [0 ],OO000000O0O000OOO .actor .infectionTimerText .color [1 ],OO000000O0O000OOO .actor .infectionTimerText .color [2 ],1.0 )
        bs .emitBGDynamics (position =OO000000O0O000OOO .actor .node .position ,velocity =OO000000O0O000OOO .actor .node .velocity ,count =int (8.0 +random .random ()*40 ),scale =1.0 ,spread =1 ,chunkType ='spark');
        if not passing :
            bs .playSound (O0000O00O00O0OO00 ._infectedSound ,1.0 ,OO000000O0O000OOO .actor .node .position )
            O0000O00O00O0OO00 .eliminationTimerDisplay =O0000O00O00O0OO00 .settings ['Elimination Timer']
            bs .gameTimer (O0000O00O00O0OO00 .settings ['Elimination Timer']*1000 ,bs .Call (O0000O00O00O0OO00 ._infectEliminate ))
            O0000O00O00O0OO00 ._infectTickTimer =bs .Timer (1000 ,bs .Call (O0000O00O00O0OO00 ._infectTick ),repeat =True )
        OO000000O0O000OOO .actor .infectionTimerText .text =str (O0000O00O00O0OO00 .eliminationTimerDisplay )
        O0000O00O00O0OO00 ._updateIcons ()
    def infectRemove (O0000O000O0O0000O ,O0OO00O000OOO00OO ):
        O0OO00O000OOO00OO .gameData ['infected']=False 
        O0OO00O000OOO00OO .actor .infectionLight .intensity =0.0 
        O0OO00O000OOO00OO .actor .infectionTimerText .color =(O0OO00O000OOO00OO .actor .infectionTimerText .color [0 ],O0OO00O000OOO00OO .actor .infectionTimerText .color [1 ],O0OO00O000OOO00OO .actor .infectionTimerText .color [2 ],0.0 )
        O0000O000O0O0000O ._updateIcons ()
    def _infectTick (O00O0000O00OO0O0O ):
        O0000OOOOO00OOO00 =None 
        for OOOO0O0OO0000O00O in O00O0000O00OO0O0O .players :
            if OOOO0O0OO0000O00O .isAlive ():pass 
            if OOOO0O0OO0000O00O .gameData ['infected']:
                O0000OOOOO00OOO00 =OOOO0O0OO0000O00O 
                break 
        if O00O0000O00OO0O0O .eliminationTimerDisplay >1 :
            if not O0000OOOOO00OOO00 :
                bs .printException ("error: tried to update the infection timer for non existent target, this shouldn't happen")
                return 
            bs .playSound (O00O0000O00OO0O0O ._tickSound ,1.0 ,O0000OOOOO00OOO00 .actor .node .position )
            O00O0000O00OO0O0O .eliminationTimerDisplay -=1 
            if O00O0000O00OO0O0O .eliminationTimerDisplay <=3 :bs .playSound (O00O0000O00OO0O0O ._dangerTickSound ,1.0 ,O0000OOOOO00OOO00 .actor .node .position )
            O0000OOOOO00OOO00 .actor .infectionTimerText .text =str (O00O0000O00OO0O0O .eliminationTimerDisplay )
        else :
            O00O0000O00OO0O0O .eliminationTimerDisplay -=1 
            O00O0000O00OO0O0O ._infectTickTimer =None 
    def _infectEliminate (O0OO000OOO00OOO00 ):
        OO00OOO00O000O0O0 =None 
        for OOO0OOO000O00O000 in O0OO000OOO00OOO00 .players :
            if OOO0OOO000O00O000 .gameData ['infected']:
                OO00OOO00O000O0O0 =OOO0OOO000O00O000 
                break 
        if not OO00OOO00O000O0O0 :
            bs .printException ("error: tried to eliminate a non-existent target, this shouldn't happen")
            return 
        OO00OOO00O000O0O0 .gameData ['infected']=False 
        OO00OOO00O000O0O0 .gameData ['eliminated']=True 
        O0OO000OOO00OOO00 ._updateIcons ()
        OO00OOO00O000O0O0 .actor .infectionTimerText .text ='TIME OUT!'
        bs .animate (OO00OOO00O000O0O0 .actor .infectionTimerText ,'scale',{0 :0.01 ,300 :0.02 ,800 :0.02 ,1200 :0.0 })
        bs .Blast (position =OO00OOO00O000O0O0 .actor .node .position ,velocity =OO00OOO00O000O0O0 .actor .node .velocity ,blastRadius =2.0 ,sourcePlayer =OO00OOO00O000O0O0 ).autoRetain ()
        bs .emitBGDynamics (position =OO00OOO00O000O0O0 .actor .node .position ,velocity =OO00OOO00O000O0O0 .actor .node .velocity ,count =int (16.0 +random .random ()*60 ),scale =1.5 ,spread =2 ,chunkType ='spark');
        OO00OOO00O000O0O0 .actor .handleMessage (bs .DieMessage (how ='infection'))
        OO00OOO00O000O0O0 .actor .shatter ()
        bs .playSound (O0OO000OOO00OOO00 ._playerEliminatedSound ,1.0 )
        OOOOOOO00OOO000OO =O0OO000OOO00OOO00 .getAlivePlayers ()
        if len (OOOOOOO00OOO000OO )==1 :
            OOOOOOO00OOO000OO [0 ].getTeam ().gameData ['survivor']=True 
            O0OO000OOO00OOO00 ._endGameTimer =bs .Timer (1000 if O0OO000OOO00OOO00 ._isSlowMotion else 1750 ,bs .WeakCall (O0OO000OOO00OOO00 .endGame ))
            return 
        def OO00000000O00000O ():
            if len (O0OO000OOO00OOO00 .players )<=1 :
                O0OO000OOO00OOO00 .endGame ()
                return 
            else :O0OO000OOO00OOO00 .infect (random .choice (OOOOOOO00OOO000OO ),False )
        O0OO000OOO00OOO00 ._infectTimer =bs .Timer (4500 ,OO00000000O00000O )
    def getAlivePlayers (OO0O00O00000000O0 ):
        O000OOOO00O0O000O =[]
        for OO000O0OO00000OOO in OO0O00O00000000O0 .players :
            if OO000O0OO00000OOO .gameData ['eliminated']:continue 
            if OO000O0OO00000OOO .isAlive ():O000OOOO00O0O000O .append (OO000O0OO00000OOO )
        return O000OOOO00O0O000O 
    def spawnPlayer (OOO000OOO00O00O00 ,O000O00000O000OOO ,oob =False ):
        OO00000OOO0O0OOOO =OOO000OOO00O00O00 .getMap ().getFFAStartPosition (OOO000OOO00O00O00 .players )
        OO00000OOO0O0OOOO =(OO00000OOO0O0OOOO [0 ],OO00000OOO0O0OOOO [1 ]-0.3 ,OO00000OOO0O0OOOO [2 ])
        OO0O0OOO000O0OO00 =None 
        O00000O000O0OOO0O =O000O00000O000OOO .getName ()
        O00O00O00OOO00O0O =bs .getNormalizedColor (O000O00000O000OOO .color )
        O00OO0O0OOO000OO0 =bs .getSafeColor (O000O00000O000OOO .color ,targetIntensity =0.75 )
        OOOO0O00O0OOO0O0O =PotatoPlayerSpaz (color =O000O00000O000OOO .color ,highlight =O000O00000O000OOO .highlight ,character =O000O00000O000OOO .character ,player =O000O00000O000OOO )
        O000O00000O000OOO .setActor (OOOO0O00O0OOO0O0O )
        OOOO0O00O0OOO0O0O .node .name =O00000O000O0OOO0O 
        OOOO0O00O0OOO0O0O .node .nameColor =O00OO0O0OOO000OO0 
        OOOO0O00O0OOO0O0O .connectControlsToPlayer ()
        OOO000OOO00O00O00 .scoreSet .playerGotNewSpaz (O000O00000O000OOO ,OOOO0O00O0OOO0O0O )
        OOOO0O00O0OOO0O0O .handleMessage (bs .StandMessage (OO00000OOO0O0OOOO ,OO0O0OOO000O0OO00 if OO0O0OOO000O0OO00 is not None else random .uniform (0 ,360 )))
        OOOOO0OO0000OO0OO =bs .getGameTime ()
        bs .playSound (OOO000OOO00O00O00 ._spawnSound ,1 ,position =OOOO0O00O0OOO0O0O .node .position )
        OOOO000O000OO0OOO =bs .newNode ('light',attrs ={'color':O00O00O00OOO00O0O })
        OOOO0O00O0OOO0O0O .node .connectAttr ('position',OOOO000O000OO0OOO ,'position')
        bs .animate (OOOO000O000OO0OOO ,'intensity',{0 :0 ,250 :1 ,500 :0 })
        bs .gameTimer (500 ,OOOO000O000OO0OOO .delete )
        try :
            if O000O00000O000OOO .gameData ['infected']:OOO000OOO00O00O00 .infect (O000O00000O000OOO )
        except KeyError :pass 
        if oob :
            if not O000O00000O000OOO .gameData ['infected']:
                O000O00000O000OOO .gameData ['fallTimes']+=1 
                bs .PopupText ("Fall Penalty!",color =(1 ,0.3 ,0 )if O000O00000O000OOO .gameData ['fallTimes']>=4 else (1 ,1 ,0 ),scale =2.0 if O000O00000O000OOO .gameData ['fallTimes']>=4 else 1.6 ,position =OOOO0O00O0OOO0O0O .node .position ).autoRetain ()
                def O0OO0O00OO0O000OO ():OOOO0O00O0OOO0O0O .node .handleMessage ("knockout",500.0 )
                if O000O00000O000OOO .gameData ['fallTimes']>=2 :bs .gameTimer (1000 ,O0OO0O00OO0O000OO )
                if O000O00000O000OOO .gameData ['fallTimes']>=4 :bs .gameTimer (2000 ,O0OO0O00OO0O000OO )
                OOOO0O00O0OOO0O0O .node .handleMessage ("knockout",500.0 )
    def handleMessage (O0OOOO0000OOO00O0 ,OO0000OO00OOOOO0O ):
        if isinstance (OO0000OO00OOOOO0O ,bs .PlayerSpazDeathMessage ):
            bs .TeamGameActivity .handleMessage (O0OOOO0000OOO00O0 ,OO0000OO00OOOOO0O )
            O00O0OOO00OO0O000 =OO0000OO00OOOOO0O .spaz .getPlayer ()
            if OO0000OO00OOOOO0O .how =='infection':
                for O0O00O0OO0OO0O0OO in O00O0OOO00OO0O000 .gameData ['icons']:
                    O0O00O0OO0OO0O0OO .handlePlayerDied ()
                return 
            O0OOOO0000OOO00O0 .spawnPlayer (O00O0OOO00OO0O000 ,True if OO0000OO00OOOOO0O .how =='fall'else False )
        else :
            super (O0OOOO0000OOO00O0 .__class__ ,O0OOOO0000OOO00O0 ).handleMessage (OO0000OO00OOOOO0O )
    def endGame (O000OOO0OO000OO00 ):
        O0OO0O0OO0OOOOOOO =bs .TeamGameResults ()
        for O0O0OOOO00O0O0000 in O000OOO0OO000OO00 .teams :O0OO0O0OO0OOOOOOO .setTeamScore (O0O0OOOO00O0O0000 ,O0O0OOOO00O0O0000 .gameData ['survivor'])
        O000OOO0OO000OO00 .end (results =O0OO0O0OO0OOOOOOO )