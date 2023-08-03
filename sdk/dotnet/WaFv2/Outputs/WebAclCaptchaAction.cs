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
    /// Checks valid token exists with request.
    /// </summary>
    [OutputType]
    public sealed class WebAclCaptchaAction
    {
        public readonly Outputs.WebAclCustomRequestHandling? CustomRequestHandling;

        [OutputConstructor]
        private WebAclCaptchaAction(Outputs.WebAclCustomRequestHandling? customRequestHandling)
        {
            CustomRequestHandling = customRequestHandling;
        }
    }
}
