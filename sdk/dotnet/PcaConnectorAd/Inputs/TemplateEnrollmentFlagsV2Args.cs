// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Inputs
{

    public sealed class TemplateEnrollmentFlagsV2Args : global::Pulumi.ResourceArgs
    {
        [Input("enableKeyReuseOnNtTokenKeysetStorageFull")]
        public Input<bool>? EnableKeyReuseOnNtTokenKeysetStorageFull { get; set; }

        [Input("includeSymmetricAlgorithms")]
        public Input<bool>? IncludeSymmetricAlgorithms { get; set; }

        [Input("noSecurityExtension")]
        public Input<bool>? NoSecurityExtension { get; set; }

        [Input("removeInvalidCertificateFromPersonalStore")]
        public Input<bool>? RemoveInvalidCertificateFromPersonalStore { get; set; }

        [Input("userInteractionRequired")]
        public Input<bool>? UserInteractionRequired { get; set; }

        public TemplateEnrollmentFlagsV2Args()
        {
        }
        public static new TemplateEnrollmentFlagsV2Args Empty => new TemplateEnrollmentFlagsV2Args();
    }
}
