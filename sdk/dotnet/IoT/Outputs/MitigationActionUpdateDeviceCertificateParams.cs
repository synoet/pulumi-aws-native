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
    /// Parameters to define a mitigation action that changes the state of the device certificate to inactive.
    /// </summary>
    [OutputType]
    public sealed class MitigationActionUpdateDeviceCertificateParams
    {
        public readonly Pulumi.AwsNative.IoT.MitigationActionUpdateDeviceCertificateParamsAction Action;

        [OutputConstructor]
        private MitigationActionUpdateDeviceCertificateParams(Pulumi.AwsNative.IoT.MitigationActionUpdateDeviceCertificateParamsAction action)
        {
            Action = action;
        }
    }
}
