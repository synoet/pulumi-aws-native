// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.AppStream.Outputs
{

    [OutputType]
    public sealed class StackFleetAssociationProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html#cfn-appstream-stackfleetassociation-fleetname
        /// </summary>
        public readonly string FleetName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html#cfn-appstream-stackfleetassociation-stackname
        /// </summary>
        public readonly string StackName;

        [OutputConstructor]
        private StackFleetAssociationProperties(
            string FleetName,

            string StackName)
        {
            this.FleetName = FleetName;
            this.StackName = StackName;
        }
    }
}