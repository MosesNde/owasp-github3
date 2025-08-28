     DataFlow::Node node1, string state1, DataFlow::Node node2, string state2
   ) {
     // create additional flow steps for `XxeFlowStateTransformer`s
    state2 = node2.asConvertedExpr().(XxeFlowStateTransformer).transform(state1) and
     DataFlow::simpleLocalFlowStep(node1, node2)
   }
 
   override predicate isBarrier(DataFlow::Node node, string flowstate) {
     // when the flowstate is transformed at a call node, block the original
     // flowstate value.
    node.asConvertedExpr().(XxeFlowStateTransformer).transform(flowstate) != flowstate
   }
 }
 