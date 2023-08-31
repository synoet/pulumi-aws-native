// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex
{
    /// <summary>
    /// A Bot Alias enables you to change the version of a bot without updating applications that use the bot
    /// </summary>
    [AwsNativeResourceType("aws-native:lex:BotAlias")]
    public partial class BotAlias : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("botAliasId")]
        public Output<string> BotAliasId { get; private set; } = null!;

        [Output("botAliasLocaleSettings")]
        public Output<ImmutableArray<Outputs.BotAliasLocaleSettingsItem>> BotAliasLocaleSettings { get; private set; } = null!;

        [Output("botAliasName")]
        public Output<string> BotAliasName { get; private set; } = null!;

        [Output("botAliasStatus")]
        public Output<Pulumi.AwsNative.Lex.BotAliasStatus> BotAliasStatus { get; private set; } = null!;

        /// <summary>
        /// A list of tags to add to the bot alias.
        /// </summary>
        [Output("botAliasTags")]
        public Output<ImmutableArray<Outputs.BotAliasTag>> BotAliasTags { get; private set; } = null!;

        [Output("botId")]
        public Output<string> BotId { get; private set; } = null!;

        [Output("botVersion")]
        public Output<string?> BotVersion { get; private set; } = null!;

        [Output("conversationLogSettings")]
        public Output<Outputs.BotAliasConversationLogSettings?> ConversationLogSettings { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
        /// </summary>
        [Output("sentimentAnalysisSettings")]
        public Output<Outputs.SentimentAnalysisSettingsProperties?> SentimentAnalysisSettings { get; private set; } = null!;


        /// <summary>
        /// Create a BotAlias resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BotAlias(string name, BotAliasArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lex:BotAlias", name, args ?? new BotAliasArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BotAlias(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lex:BotAlias", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "botId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BotAlias resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BotAlias Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new BotAlias(name, id, options);
        }
    }

    public sealed class BotAliasArgs : global::Pulumi.ResourceArgs
    {
        [Input("botAliasLocaleSettings")]
        private InputList<Inputs.BotAliasLocaleSettingsItemArgs>? _botAliasLocaleSettings;
        public InputList<Inputs.BotAliasLocaleSettingsItemArgs> BotAliasLocaleSettings
        {
            get => _botAliasLocaleSettings ?? (_botAliasLocaleSettings = new InputList<Inputs.BotAliasLocaleSettingsItemArgs>());
            set => _botAliasLocaleSettings = value;
        }

        [Input("botAliasName")]
        public Input<string>? BotAliasName { get; set; }

        [Input("botAliasTags")]
        private InputList<Inputs.BotAliasTagArgs>? _botAliasTags;

        /// <summary>
        /// A list of tags to add to the bot alias.
        /// </summary>
        public InputList<Inputs.BotAliasTagArgs> BotAliasTags
        {
            get => _botAliasTags ?? (_botAliasTags = new InputList<Inputs.BotAliasTagArgs>());
            set => _botAliasTags = value;
        }

        [Input("botId", required: true)]
        public Input<string> BotId { get; set; } = null!;

        [Input("botVersion")]
        public Input<string>? BotVersion { get; set; }

        [Input("conversationLogSettings")]
        public Input<Inputs.BotAliasConversationLogSettingsArgs>? ConversationLogSettings { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
        /// </summary>
        [Input("sentimentAnalysisSettings")]
        public Input<Inputs.SentimentAnalysisSettingsPropertiesArgs>? SentimentAnalysisSettings { get; set; }

        public BotAliasArgs()
        {
        }
        public static new BotAliasArgs Empty => new BotAliasArgs();
    }
}
