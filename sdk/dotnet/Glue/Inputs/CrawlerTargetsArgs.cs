// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    public sealed class CrawlerTargetsArgs : global::Pulumi.ResourceArgs
    {
        [Input("catalogTargets")]
        private InputList<Inputs.CrawlerCatalogTargetArgs>? _catalogTargets;
        public InputList<Inputs.CrawlerCatalogTargetArgs> CatalogTargets
        {
            get => _catalogTargets ?? (_catalogTargets = new InputList<Inputs.CrawlerCatalogTargetArgs>());
            set => _catalogTargets = value;
        }

        [Input("deltaTargets")]
        private InputList<Inputs.CrawlerDeltaTargetArgs>? _deltaTargets;
        public InputList<Inputs.CrawlerDeltaTargetArgs> DeltaTargets
        {
            get => _deltaTargets ?? (_deltaTargets = new InputList<Inputs.CrawlerDeltaTargetArgs>());
            set => _deltaTargets = value;
        }

        [Input("dynamoDbTargets")]
        private InputList<Inputs.CrawlerDynamoDBTargetArgs>? _dynamoDbTargets;
        public InputList<Inputs.CrawlerDynamoDBTargetArgs> DynamoDbTargets
        {
            get => _dynamoDbTargets ?? (_dynamoDbTargets = new InputList<Inputs.CrawlerDynamoDBTargetArgs>());
            set => _dynamoDbTargets = value;
        }

        [Input("jdbcTargets")]
        private InputList<Inputs.CrawlerJdbcTargetArgs>? _jdbcTargets;
        public InputList<Inputs.CrawlerJdbcTargetArgs> JdbcTargets
        {
            get => _jdbcTargets ?? (_jdbcTargets = new InputList<Inputs.CrawlerJdbcTargetArgs>());
            set => _jdbcTargets = value;
        }

        [Input("mongoDbTargets")]
        private InputList<Inputs.CrawlerMongoDBTargetArgs>? _mongoDbTargets;
        public InputList<Inputs.CrawlerMongoDBTargetArgs> MongoDbTargets
        {
            get => _mongoDbTargets ?? (_mongoDbTargets = new InputList<Inputs.CrawlerMongoDBTargetArgs>());
            set => _mongoDbTargets = value;
        }

        [Input("s3Targets")]
        private InputList<Inputs.CrawlerS3TargetArgs>? _s3Targets;
        public InputList<Inputs.CrawlerS3TargetArgs> S3Targets
        {
            get => _s3Targets ?? (_s3Targets = new InputList<Inputs.CrawlerS3TargetArgs>());
            set => _s3Targets = value;
        }

        public CrawlerTargetsArgs()
        {
        }
        public static new CrawlerTargetsArgs Empty => new CrawlerTargetsArgs();
    }
}
