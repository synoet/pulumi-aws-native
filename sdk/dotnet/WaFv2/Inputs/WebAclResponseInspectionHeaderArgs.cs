// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Inputs
{

    /// <summary>
    /// Response headers that indicate success or failure of a login request
    /// </summary>
    public sealed class WebAclResponseInspectionHeaderArgs : global::Pulumi.ResourceArgs
    {
        [Input("failureValues", required: true)]
        private InputList<string>? _failureValues;
        public InputList<string> FailureValues
        {
            get => _failureValues ?? (_failureValues = new InputList<string>());
            set => _failureValues = value;
        }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("successValues", required: true)]
        private InputList<string>? _successValues;
        public InputList<string> SuccessValues
        {
            get => _successValues ?? (_successValues = new InputList<string>());
            set => _successValues = value;
        }

        public WebAclResponseInspectionHeaderArgs()
        {
        }
        public static new WebAclResponseInspectionHeaderArgs Empty => new WebAclResponseInspectionHeaderArgs();
    }
}
