// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Kendra.Outputs
{

    [OutputType]
    public sealed class DataSourceConfluenceBlogConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html#cfn-kendra-datasource-confluenceblogconfiguration-blogfieldmappings
        /// </summary>
        public readonly Outputs.DataSourceConfluenceBlogFieldMappingsList? BlogFieldMappings;

        [OutputConstructor]
        private DataSourceConfluenceBlogConfiguration(Outputs.DataSourceConfluenceBlogFieldMappingsList? BlogFieldMappings)
        {
            this.BlogFieldMappings = BlogFieldMappings;
        }
    }
}