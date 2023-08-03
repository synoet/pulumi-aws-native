// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Outputs
{

    /// <summary>
    /// Parameters to define a mitigation action that changes the state of the CA certificate to inactive.
    /// </summary>
    [OutputType]
    public sealed class MitigationActionUpdateCaCertificateParams
    {
        public readonly Pulumi.AwsNative.IoT.MitigationActionUpdateCaCertificateParamsAction Action;

        [OutputConstructor]
        private MitigationActionUpdateCaCertificateParams(Pulumi.AwsNative.IoT.MitigationActionUpdateCaCertificateParamsAction action)
        {
            Action = action;
        }
    }
}
