// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Outputs
{

    [OutputType]
    public sealed class DataSourceSalesforceKnowledgeArticleConfiguration
    {
        public readonly ImmutableArray<Outputs.DataSourceSalesforceCustomKnowledgeArticleTypeConfiguration> CustomKnowledgeArticleTypeConfigurations;
        public readonly ImmutableArray<Pulumi.AwsNative.Kendra.DataSourceSalesforceKnowledgeArticleState> IncludedStates;
        public readonly Outputs.DataSourceSalesforceStandardKnowledgeArticleTypeConfiguration? StandardKnowledgeArticleTypeConfiguration;

        [OutputConstructor]
        private DataSourceSalesforceKnowledgeArticleConfiguration(
            ImmutableArray<Outputs.DataSourceSalesforceCustomKnowledgeArticleTypeConfiguration> customKnowledgeArticleTypeConfigurations,

            ImmutableArray<Pulumi.AwsNative.Kendra.DataSourceSalesforceKnowledgeArticleState> includedStates,

            Outputs.DataSourceSalesforceStandardKnowledgeArticleTypeConfiguration? standardKnowledgeArticleTypeConfiguration)
        {
            CustomKnowledgeArticleTypeConfigurations = customKnowledgeArticleTypeConfigurations;
            IncludedStates = includedStates;
            StandardKnowledgeArticleTypeConfiguration = standardKnowledgeArticleTypeConfiguration;
        }
    }
}
