// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Greengrass.Outputs
{

    [OutputType]
    public sealed class CoreDefinitionCore
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-certificatearn
        /// </summary>
        public readonly string CertificateArn;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-id
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-syncshadow
        /// </summary>
        public readonly bool? SyncShadow;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-thingarn
        /// </summary>
        public readonly string ThingArn;

        [OutputConstructor]
        private CoreDefinitionCore(
            string CertificateArn,

            string Id,

            bool? SyncShadow,

            string ThingArn)
        {
            this.CertificateArn = CertificateArn;
            this.Id = Id;
            this.SyncShadow = SyncShadow;
            this.ThingArn = ThingArn;
        }
    }
}