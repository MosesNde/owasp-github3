     // constructor.
     exists(CallInstruction call |
       call.getStaticCallTarget() = any(XercesDomParserClass c).getAConstructor() and
      node.asInstruction().(WriteSideEffectInstruction).getDestinationAddress() =
        call.getThisArgument() and
       encodeXercesFlowState(flowstate, 0, 1) // default configuration
     )
   }
     // constructor.
     exists(CallInstruction call |
       call.getStaticCallTarget() = any(SaxParserClass c).getAConstructor() and
      node.asInstruction().(WriteSideEffectInstruction).getDestinationAddress() =
        call.getThisArgument() and
       encodeXercesFlowState(flowstate, 0, 1) // default configuration
     )
   }