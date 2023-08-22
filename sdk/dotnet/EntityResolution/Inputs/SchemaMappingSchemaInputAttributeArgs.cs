// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EntityResolution.Inputs
{

    public sealed class SchemaMappingSchemaInputAttributeArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldName", required: true)]
        public Input<string> FieldName { get; set; } = null!;

        [Input("groupName")]
        public Input<string>? GroupName { get; set; }

        [Input("matchKey")]
        public Input<string>? MatchKey { get; set; }

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.EntityResolution.SchemaMappingSchemaAttributeType> Type { get; set; } = null!;

        public SchemaMappingSchemaInputAttributeArgs()
        {
        }
        public static new SchemaMappingSchemaInputAttributeArgs Empty => new SchemaMappingSchemaInputAttributeArgs();
    }
}
