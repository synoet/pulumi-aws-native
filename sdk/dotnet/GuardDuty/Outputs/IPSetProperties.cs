// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.GuardDuty.Outputs
{

    [OutputType]
    public sealed class IPSetProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        /// </summary>
        public readonly bool Activate;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        /// </summary>
        public readonly string DetectorId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        /// </summary>
        public readonly string Format;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private IPSetProperties(
            bool Activate,

            string DetectorId,

            string Format,

            string Location,

            string? Name)
        {
            this.Activate = Activate;
            this.DetectorId = DetectorId;
            this.Format = Format;
            this.Location = Location;
            this.Name = Name;
        }
    }
}