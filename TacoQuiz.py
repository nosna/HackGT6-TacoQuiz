# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.

# version 1401
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class GlobalStorage:
    
    def __init__(self, i, vocab_num):
        self.i = i
        self.vocab_num = vocab_num
    
    def set_i(self, i):
        self.i = i
    
    def get_i(self):
        return self.i
    
    def get_vocab_num(self):
        return self.vocab_num
    
    def set_vocab_num(self, vocab_num):
        self.vocab_num = vocab_num

gs = GlobalStorage(0, -1)

englishWords = [
    "hello",
    "good",
    "bye",
    "thanks",
    "only",
    "I",
    "my",
    "spanish",
    "yes",
    "book",
    "incorrect",
    "pretty",
    "five",
    "day",
    "water",
    "love",
    "years",
    "history",
    "curious",
    "home"
]

spanishWords = [ # including weird pronounciations
    ["hola", "ola"],
    ["bien", "beard", "b.n."],
    ["adios"],
    ["gracias"],
    ["solo"],
    ["yo","your", "you are", "you're", "you"],
    ["mi", "me"],
    ["espanol"],
    ["si", "c", "sea"],
    ["libro", "libreal", "libra"],
    ["incorrecto", "incorrect to", "incorrect"],
    ["bonito"],
    ["cinco", "single"],
    ["dia", "t.a."],
    ["agua", "aqua", "i wanna"],
    ["amor", "are more"],
    ["anos", "announce"],
    ["historia", "his terraria"],
    ["curioso", "curiosity"],
    ["casa", "kasa"]
    
]

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        gs.set_vocab_num(-1)
        speak_output = "Hola! A taco a day, keeps the bad grade away. Let's Taco some basic Spanish vocabulary quizzes. We have 20 vocabs in the word bank. How many vocabs would you like to Taco today?"
        reprompt_text = "How many vocabs would you like to taco today?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )


class CaptureVocabNumIntentHandler(AbstractRequestHandler):
    """Handler for Capture Vocab Num Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureVocabNumIntent")(handler_input)
       

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        gs.set_vocab_num(int(slots["vocab_num"].value))
        if gs.get_vocab_num() > 20:
            speak_output = "You have too many tacos. How many vocabs would you like to taco today?"
        elif gs.get_vocab_num() <= 0:
            speak_output = "You have to get some tacos. How many vocabs would you like to taco today?"
        else:
            speak_output = "Okay. {} vocabs it is. You can say \"start\" to begin Tacoling".format(gs.get_vocab_num())
        
        handler_input.response_builder.speak(speak_output)
        handler_input.response_builder.ask(speak_output)
        # .ask("add a reprompt if you want to keep the session open for the user to respond")
        return handler_input.response_builder.response

class StartQuizIntentHandler(AbstractRequestHandler):
    """Handler for Start Quiz Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StartQuizIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # slots = handler_input.request_envelope.request.intent.slots
        speak_output = "What's {} in Spanish?".format(englishWords[gs.get_i() % len(englishWords)])
        handler_input.response_builder.speak(speak_output)
        handler_input.response_builder.ask(speak_output)
        return handler_input.response_builder.response

class NewQuestionIntentHandler(AbstractRequestHandler):
    """Handler for New Question Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NewQuestionIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        next_word = englishWords[gs.get_i() % len(englishWords)]
        speak_output = "What's {} in Spanish?".format(next_word)
        handler_input.response_builder.speak(speak_output)
        handler_input.response_builder.ask(speak_output)
        return handler_input.response_builder.response

class CheckVocabIntentHandler(AbstractRequestHandler):
    """Handler for Check Vocab Intent."""
    asked = False
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CheckVocabIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        vocab = slots["vocab"].value
        # check if input is correct
        speak_output = ""
        if str(vocab).lower() in spanishWords[gs.get_i() % len(englishWords)]:
            speak_output = "{} is correct. You can say \"more tacos\" for the next question".format(vocab)
            gs.set_i(gs.get_i() + 1)
            gs.set_vocab_num(gs.get_vocab_num() - 1)
        else:
            if CheckVocabIntentHandler.asked:
                speak_output = "The correct answer is {}. You can say \"more tacos\" for the next question".format(spanishWords[gs.get_i()][0])
                gs.set_i(gs.get_i() + 1)
            else:
                CheckVocabIntentHandler.asked = True
                return handler_input.response_builder.speak("Try again, mi amigo.").ask("Try again, mi amigo.").response
        CheckVocabIntentHandler.asked = False
        return handler_input.response_builder.speak(speak_output).ask(speak_output).response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input)) or gs.get_vocab_num() == 0

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Adios, mi amigo!"
        if gs.get_vocab_num() == 0:
            speak_output = "You TACO them all. Buen trabajo!"
        gs.set_i(0)
        gs.set_vocab_num(-1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Any cleanup logic goes here.
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureVocabNumIntentHandler())
sb.add_request_handler(StartQuizIntentHandler())
sb.add_request_handler(CheckVocabIntentHandler())
sb.add_request_handler(NewQuestionIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
