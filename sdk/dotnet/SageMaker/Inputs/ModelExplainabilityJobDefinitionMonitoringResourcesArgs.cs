// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SageMaker.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html
    /// </summary>
    public sealed class ModelExplainabilityJobDefinitionMonitoringResourcesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig
        /// </summary>
        [Input("ClusterConfig", required: true)]
        public Input<Inputs.ModelExplainabilityJobDefinitionClusterConfigArgs> ClusterConfig { get; set; } = null!;

        public ModelExplainabilityJobDefinitionMonitoringResourcesArgs()
        {
        }
    }
}