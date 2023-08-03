// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    /// <summary>
    /// Configures how to use the Account Takeover Prevention managed rule group in the web ACL
    /// </summary>
    [OutputType]
    public sealed class WebAclAwsManagedRulesAtpRuleSet
    {
        public readonly bool? EnableRegexInPath;
        public readonly string LoginPath;
        public readonly Outputs.WebAclRequestInspection? RequestInspection;
        public readonly Outputs.WebAclResponseInspection? ResponseInspection;

        [OutputConstructor]
        private WebAclAwsManagedRulesAtpRuleSet(
            bool? enableRegexInPath,

            string loginPath,

            Outputs.WebAclRequestInspection? requestInspection,

            Outputs.WebAclResponseInspection? responseInspection)
        {
            EnableRegexInPath = enableRegexInPath;
            LoginPath = loginPath;
            RequestInspection = requestInspection;
            ResponseInspection = responseInspection;
        }
    }
}
