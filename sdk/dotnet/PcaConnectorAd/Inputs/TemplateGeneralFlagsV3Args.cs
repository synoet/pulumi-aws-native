// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Inputs
{

    public sealed class TemplateGeneralFlagsV3Args : global::Pulumi.ResourceArgs
    {
        [Input("autoEnrollment")]
        public Input<bool>? AutoEnrollment { get; set; }

        [Input("machineType")]
        public Input<bool>? MachineType { get; set; }

        public TemplateGeneralFlagsV3Args()
        {
        }
        public static new TemplateGeneralFlagsV3Args Empty => new TemplateGeneralFlagsV3Args();
    }
}
