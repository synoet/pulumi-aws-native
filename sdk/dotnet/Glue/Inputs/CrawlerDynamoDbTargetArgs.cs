// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    public sealed class CrawlerDynamoDbTargetArgs : global::Pulumi.ResourceArgs
    {
        [Input("path")]
        public Input<string>? Path { get; set; }

        public CrawlerDynamoDbTargetArgs()
        {
        }
        public static new CrawlerDynamoDbTargetArgs Empty => new CrawlerDynamoDbTargetArgs();
    }
}
