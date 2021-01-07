// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SageMaker.Outputs
{

    [OutputType]
    public sealed class DataQualityJobDefinitionProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification
        /// </summary>
        public readonly Outputs.DataQualityJobDefinitionDataQualityAppSpecification DataQualityAppSpecification;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig
        /// </summary>
        public readonly Outputs.DataQualityJobDefinitionDataQualityBaselineConfig? DataQualityBaselineConfig;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput
        /// </summary>
        public readonly Outputs.DataQualityJobDefinitionDataQualityJobInput DataQualityJobInput;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig
        /// </summary>
        public readonly Outputs.DataQualityJobDefinitionMonitoringOutputConfig DataQualityJobOutputConfig;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname
        /// </summary>
        public readonly string? JobDefinitionName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources
        /// </summary>
        public readonly Outputs.DataQualityJobDefinitionMonitoringResources JobResources;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig
        /// </summary>
        public readonly Outputs.DataQualityJobDefinitionNetworkConfig? NetworkConfig;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn
        /// </summary>
        public readonly string RoleArn;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition
        /// </summary>
        public readonly Outputs.DataQualityJobDefinitionStoppingCondition? StoppingCondition;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags
        /// </summary>
        public readonly ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags;

        [OutputConstructor]
        private DataQualityJobDefinitionProperties(
            Outputs.DataQualityJobDefinitionDataQualityAppSpecification DataQualityAppSpecification,

            Outputs.DataQualityJobDefinitionDataQualityBaselineConfig? DataQualityBaselineConfig,

            Outputs.DataQualityJobDefinitionDataQualityJobInput DataQualityJobInput,

            Outputs.DataQualityJobDefinitionMonitoringOutputConfig DataQualityJobOutputConfig,

            string? JobDefinitionName,

            Outputs.DataQualityJobDefinitionMonitoringResources JobResources,

            Outputs.DataQualityJobDefinitionNetworkConfig? NetworkConfig,

            string RoleArn,

            Outputs.DataQualityJobDefinitionStoppingCondition? StoppingCondition,

            ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags)
        {
            this.DataQualityAppSpecification = DataQualityAppSpecification;
            this.DataQualityBaselineConfig = DataQualityBaselineConfig;
            this.DataQualityJobInput = DataQualityJobInput;
            this.DataQualityJobOutputConfig = DataQualityJobOutputConfig;
            this.JobDefinitionName = JobDefinitionName;
            this.JobResources = JobResources;
            this.NetworkConfig = NetworkConfig;
            this.RoleArn = RoleArn;
            this.StoppingCondition = StoppingCondition;
            this.Tags = Tags;
        }
    }
}