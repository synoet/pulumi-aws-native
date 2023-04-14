// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    /// <summary>
    /// Response status codes that indicate success or failure of a login request
    /// </summary>
    public sealed class WebACLResponseInspectionStatusCodeArgs : global::Pulumi.ResourceArgs
    {
        [Input("failureCodes", required: true)]
        private InputList<int>? _failureCodes;
        public InputList<int> FailureCodes
        {
            get => _failureCodes ?? (_failureCodes = new InputList<int>());
            set => _failureCodes = value;
        }

        [Input("successCodes", required: true)]
        private InputList<int>? _successCodes;
        public InputList<int> SuccessCodes
        {
            get => _successCodes ?? (_successCodes = new InputList<int>());
            set => _successCodes = value;
        }

        public WebACLResponseInspectionStatusCodeArgs()
        {
        }
        public static new WebACLResponseInspectionStatusCodeArgs Empty => new WebACLResponseInspectionStatusCodeArgs();
    }
}
