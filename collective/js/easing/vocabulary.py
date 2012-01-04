from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.i18nmessageid import MessageFactory
messageFactory = MessageFactory('collective.fancyboxgallery')
_ = messageFactory

easings = SimpleVocabulary(
    [SimpleTerm(value=u'swing',       title=_(u'swing')),
     SimpleTerm(value=u'easeInQuad',       title=_(u'easeInQuad')),
     SimpleTerm(value=u'easeOutQuad',      title=_(u'easeOutQuad')),
     SimpleTerm(value=u'easeInOutQuad',    title=_(u'easeInOutQuad')),
     SimpleTerm(value=u'easeInCubic',      title=_(u'easeInCubic')),
     SimpleTerm(value=u'easeOutCubic',     title=_(u'easeOutCubic')),
     SimpleTerm(value=u'easeInOutCubic',   title=_(u'easeInOutCubic')),
     SimpleTerm(value=u'easeInQuart',      title=_(u'easeInQuart')),
     SimpleTerm(value=u'easeOutQuart',     title=_(u'easeOutQuart')),
     SimpleTerm(value=u'easeInOutQuart',   title=_(u'easeInOutQuart')),
     SimpleTerm(value=u'easeInQuint',      title=_(u'easeInQuint')),
     SimpleTerm(value=u'easeOutQuint',     title=_(u'easeOutQuint')),
     SimpleTerm(value=u'easeInOutQuint',   title=_(u'easeInOutQuint')),
     SimpleTerm(value=u'easeInSine',       title=_(u'easeInSine')),
     SimpleTerm(value=u'easeOutSine',      title=_(u'easeOutSine')),
     SimpleTerm(value=u'easeInOutSine',    title=_(u'easeInOutSine')),
     SimpleTerm(value=u'easeInExpo',       title=_(u'easeInExpo')),
     SimpleTerm(value=u'easeOutExpo',      title=_(u'easeOutExpo')),
     SimpleTerm(value=u'easeInOutExpo',    title=_(u'easeInOutExpo')),
     SimpleTerm(value=u'easeInCirc',       title=_(u'easeInCirc')),
     SimpleTerm(value=u'easeOutCirc',      title=_(u'easeOutCirc')),
     SimpleTerm(value=u'easeInOutCirc',    title=_(u'easeInOutCirc')),
     SimpleTerm(value=u'easeInElastic',    title=_(u'easeInElastic')),
     SimpleTerm(value=u'easeOutElastic',   title=_(u'easeOutElastic')),
     SimpleTerm(value=u'easeInOutElastic', title=_(u'easeInOutElastic')),
     SimpleTerm(value=u'easeInBack',       title=_(u'easeInBack')),
     SimpleTerm(value=u'easeOutBack',      title=_(u'easeOutBack')),
     SimpleTerm(value=u'easeInOutBack',    title=_(u'easeInOutBack')),
     SimpleTerm(value=u'easeInBounce',     title=_(u'easeInBounce')),
     SimpleTerm(value=u'easeOutBounce',    title=_(u'easeOutBounce')),
     SimpleTerm(value=u'easeInOutBounce',  title=_(u'easeInOutBounce'))]
    )
