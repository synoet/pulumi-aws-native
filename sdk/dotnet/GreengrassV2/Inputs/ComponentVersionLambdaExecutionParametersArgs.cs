// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GreengrassV2.Inputs
{

    public sealed class ComponentVersionLambdaExecutionParametersArgs : Pulumi.ResourceArgs
    {
        [Input("environmentVariables")]
        public Input<object>? EnvironmentVariables { get; set; }

        [Input("eventSources")]
        private InputList<Inputs.ComponentVersionLambdaEventSourceArgs>? _eventSources;
        public InputList<Inputs.ComponentVersionLambdaEventSourceArgs> EventSources
        {
            get => _eventSources ?? (_eventSources = new InputList<Inputs.ComponentVersionLambdaEventSourceArgs>());
            set => _eventSources = value;
        }

        [Input("execArgs")]
        private InputList<string>? _execArgs;
        public InputList<string> ExecArgs
        {
            get => _execArgs ?? (_execArgs = new InputList<string>());
            set => _execArgs = value;
        }

        [Input("inputPayloadEncodingType")]
        public Input<Pulumi.AwsNative.GreengrassV2.ComponentVersionLambdaExecutionParametersInputPayloadEncodingType>? InputPayloadEncodingType { get; set; }

        [Input("linuxProcessParams")]
        public Input<Inputs.ComponentVersionLambdaLinuxProcessParamsArgs>? LinuxProcessParams { get; set; }

        [Input("maxIdleTimeInSeconds")]
        public Input<int>? MaxIdleTimeInSeconds { get; set; }

        [Input("maxInstancesCount")]
        public Input<int>? MaxInstancesCount { get; set; }

        [Input("maxQueueSize")]
        public Input<int>? MaxQueueSize { get; set; }

        [Input("pinned")]
        public Input<bool>? Pinned { get; set; }

        [Input("statusTimeoutInSeconds")]
        public Input<int>? StatusTimeoutInSeconds { get; set; }

        [Input("timeoutInSeconds")]
        public Input<int>? TimeoutInSeconds { get; set; }

        public ComponentVersionLambdaExecutionParametersArgs()
        {
        }
    }
}
