// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Dlm.Outputs
{

    [OutputType]
    public sealed class LifecyclePolicyScript
    {
        public readonly bool? ExecuteOperationOnScriptFailure;
        public readonly string? ExecutionHandler;
        public readonly string? ExecutionHandlerService;
        public readonly int? ExecutionTimeout;
        public readonly int? MaximumRetryCount;
        public readonly ImmutableArray<string> Stages;

        [OutputConstructor]
        private LifecyclePolicyScript(
            bool? executeOperationOnScriptFailure,

            string? executionHandler,

            string? executionHandlerService,

            int? executionTimeout,

            int? maximumRetryCount,

            ImmutableArray<string> stages)
        {
            ExecuteOperationOnScriptFailure = executeOperationOnScriptFailure;
            ExecutionHandler = executionHandler;
            ExecutionHandlerService = executionHandlerService;
            ExecutionTimeout = executionTimeout;
            MaximumRetryCount = maximumRetryCount;
            Stages = stages;
        }
    }
}
