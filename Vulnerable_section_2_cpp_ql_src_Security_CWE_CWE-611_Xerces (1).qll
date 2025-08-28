   override predicate configurationSource(DataFlow::Node node, string flowstate) {
     // source is the write on `this` of a call to the `XercesDOMParser`
     // constructor.
    exists(CallInstruction call |
      call.getStaticCallTarget() = any(XercesDomParserClass c).getAConstructor() and
      node.asInstruction().(StoreInstruction).getSourceValue() = call.getThisArgument() and
       encodeXercesFlowState(flowstate, 0, 1) // default configuration
     )
   }
     // sink is the read of the qualifier of a call to `AbstractDOMParser.parse`.
     exists(Call call |
       call.getTarget().getClassAndName("parse") instanceof AbstractDomParserClass and
      call.getQualifier() = node.asConvertedExpr()
     ) and
     flowstate instanceof XercesFlowState and
     not encodeXercesFlowState(flowstate, 1, 1) // safe configuration
     // source is the result of a call to `createLSParser`.
     exists(Call call |
       call.getTarget() instanceof CreateLSParser and
      call = node.asExpr() and
       encodeXercesFlowState(flowstate, 0, 1) // default configuration
     )
   }
     // sink is the read of the qualifier of a call to `DOMLSParserClass.parse`.
     exists(Call call |
       call.getTarget().getClassAndName("parse") instanceof DomLSParserClass and
      call.getQualifier() = node.asConvertedExpr()
     ) and
     flowstate instanceof XercesFlowState and
     not encodeXercesFlowState(flowstate, 1, 1) // safe configuration
   override predicate configurationSource(DataFlow::Node node, string flowstate) {
     // source is the write on `this` of a call to the `SAXParser`
     // constructor.
    exists(CallInstruction call |
      call.getStaticCallTarget() = any(SaxParserClass c).getAConstructor() and
      node.asInstruction().(StoreInstruction).getSourceValue() = call.getThisArgument() and
       encodeXercesFlowState(flowstate, 0, 1) // default configuration
     )
   }
     // sink is the read of the qualifier of a call to `SAXParser.parse`.
     exists(Call call |
       call.getTarget().getClassAndName("parse") instanceof SaxParserClass and
      call.getQualifier() = node.asConvertedExpr()
     ) and
     flowstate instanceof XercesFlowState and
     not encodeXercesFlowState(flowstate, 1, 1) // safe configuration
     // source is the result of a call to `createXMLReader`.
     exists(Call call |
       call.getTarget() instanceof CreateXmlReader and
      call = node.asExpr() and
       encodeXercesFlowState(flowstate, 0, 1) // default configuration
     )
   }
     // sink is the read of the qualifier of a call to `SAX2XMLReader.parse`.
     exists(Call call |
       call.getTarget().getClassAndName("parse") instanceof Sax2XmlReader and
      call.getQualifier() = node.asConvertedExpr()
     ) and
     flowstate instanceof XercesFlowState and
     not encodeXercesFlowState(flowstate, 1, 1) // safe configuration