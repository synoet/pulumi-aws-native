// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Glue.Outputs
{

    [OutputType]
    public sealed class CrawlerDynamoDBTarget
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html#cfn-glue-crawler-dynamodbtarget-path
        /// </summary>
        public readonly string? Path;

        [OutputConstructor]
        private CrawlerDynamoDBTarget(string? Path)
        {
            this.Path = Path;
        }
    }
}