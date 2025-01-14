// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TopicNamedEntity
    {
        public readonly ImmutableArray<Outputs.TopicNamedEntityDefinition> Definition;
        public readonly string? EntityDescription;
        public readonly string EntityName;
        public readonly ImmutableArray<string> EntitySynonyms;
        public readonly Outputs.TopicSemanticEntityType? SemanticEntityType;

        [OutputConstructor]
        private TopicNamedEntity(
            ImmutableArray<Outputs.TopicNamedEntityDefinition> definition,

            string? entityDescription,

            string entityName,

            ImmutableArray<string> entitySynonyms,

            Outputs.TopicSemanticEntityType? semanticEntityType)
        {
            Definition = definition;
            EntityDescription = entityDescription;
            EntityName = entityName;
            EntitySynonyms = entitySynonyms;
            SemanticEntityType = semanticEntityType;
        }
    }
}
