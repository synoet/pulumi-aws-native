// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.IoTSiteWise.Outputs
{

    [OutputType]
    public sealed class AssetModelVariableValue
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-hierarchylogicalid
        /// </summary>
        public readonly string? HierarchyLogicalId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-propertylogicalid
        /// </summary>
        public readonly string PropertyLogicalId;

        [OutputConstructor]
        private AssetModelVariableValue(
            string? HierarchyLogicalId,

            string PropertyLogicalId)
        {
            this.HierarchyLogicalId = HierarchyLogicalId;
            this.PropertyLogicalId = PropertyLogicalId;
        }
    }
}