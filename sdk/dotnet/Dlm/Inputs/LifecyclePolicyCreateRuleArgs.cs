// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Dlm.Inputs
{

    public sealed class LifecyclePolicyCreateRuleArgs : global::Pulumi.ResourceArgs
    {
        [Input("cronExpression")]
        public Input<string>? CronExpression { get; set; }

        [Input("interval")]
        public Input<int>? Interval { get; set; }

        [Input("intervalUnit")]
        public Input<string>? IntervalUnit { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("scripts")]
        private InputList<Inputs.LifecyclePolicyScriptArgs>? _scripts;
        public InputList<Inputs.LifecyclePolicyScriptArgs> Scripts
        {
            get => _scripts ?? (_scripts = new InputList<Inputs.LifecyclePolicyScriptArgs>());
            set => _scripts = value;
        }

        [Input("times")]
        private InputList<string>? _times;
        public InputList<string> Times
        {
            get => _times ?? (_times = new InputList<string>());
            set => _times = value;
        }

        public LifecyclePolicyCreateRuleArgs()
        {
        }
        public static new LifecyclePolicyCreateRuleArgs Empty => new LifecyclePolicyCreateRuleArgs();
    }
}
