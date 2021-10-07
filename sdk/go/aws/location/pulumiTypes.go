// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package location

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type MapConfiguration struct {
	Style string `pulumi:"style"`
}

// MapConfigurationInput is an input type that accepts MapConfigurationArgs and MapConfigurationOutput values.
// You can construct a concrete instance of `MapConfigurationInput` via:
//
//          MapConfigurationArgs{...}
type MapConfigurationInput interface {
	pulumi.Input

	ToMapConfigurationOutput() MapConfigurationOutput
	ToMapConfigurationOutputWithContext(context.Context) MapConfigurationOutput
}

type MapConfigurationArgs struct {
	Style pulumi.StringInput `pulumi:"style"`
}

func (MapConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*MapConfiguration)(nil)).Elem()
}

func (i MapConfigurationArgs) ToMapConfigurationOutput() MapConfigurationOutput {
	return i.ToMapConfigurationOutputWithContext(context.Background())
}

func (i MapConfigurationArgs) ToMapConfigurationOutputWithContext(ctx context.Context) MapConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MapConfigurationOutput)
}

func (i MapConfigurationArgs) ToMapConfigurationPtrOutput() MapConfigurationPtrOutput {
	return i.ToMapConfigurationPtrOutputWithContext(context.Background())
}

func (i MapConfigurationArgs) ToMapConfigurationPtrOutputWithContext(ctx context.Context) MapConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MapConfigurationOutput).ToMapConfigurationPtrOutputWithContext(ctx)
}

// MapConfigurationPtrInput is an input type that accepts MapConfigurationArgs, MapConfigurationPtr and MapConfigurationPtrOutput values.
// You can construct a concrete instance of `MapConfigurationPtrInput` via:
//
//          MapConfigurationArgs{...}
//
//  or:
//
//          nil
type MapConfigurationPtrInput interface {
	pulumi.Input

	ToMapConfigurationPtrOutput() MapConfigurationPtrOutput
	ToMapConfigurationPtrOutputWithContext(context.Context) MapConfigurationPtrOutput
}

type mapConfigurationPtrType MapConfigurationArgs

func MapConfigurationPtr(v *MapConfigurationArgs) MapConfigurationPtrInput {
	return (*mapConfigurationPtrType)(v)
}

func (*mapConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**MapConfiguration)(nil)).Elem()
}

func (i *mapConfigurationPtrType) ToMapConfigurationPtrOutput() MapConfigurationPtrOutput {
	return i.ToMapConfigurationPtrOutputWithContext(context.Background())
}

func (i *mapConfigurationPtrType) ToMapConfigurationPtrOutputWithContext(ctx context.Context) MapConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MapConfigurationPtrOutput)
}

type MapConfigurationOutput struct{ *pulumi.OutputState }

func (MapConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MapConfiguration)(nil)).Elem()
}

func (o MapConfigurationOutput) ToMapConfigurationOutput() MapConfigurationOutput {
	return o
}

func (o MapConfigurationOutput) ToMapConfigurationOutputWithContext(ctx context.Context) MapConfigurationOutput {
	return o
}

func (o MapConfigurationOutput) ToMapConfigurationPtrOutput() MapConfigurationPtrOutput {
	return o.ToMapConfigurationPtrOutputWithContext(context.Background())
}

func (o MapConfigurationOutput) ToMapConfigurationPtrOutputWithContext(ctx context.Context) MapConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v MapConfiguration) *MapConfiguration {
		return &v
	}).(MapConfigurationPtrOutput)
}

func (o MapConfigurationOutput) Style() pulumi.StringOutput {
	return o.ApplyT(func(v MapConfiguration) string { return v.Style }).(pulumi.StringOutput)
}

type MapConfigurationPtrOutput struct{ *pulumi.OutputState }

func (MapConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MapConfiguration)(nil)).Elem()
}

func (o MapConfigurationPtrOutput) ToMapConfigurationPtrOutput() MapConfigurationPtrOutput {
	return o
}

func (o MapConfigurationPtrOutput) ToMapConfigurationPtrOutputWithContext(ctx context.Context) MapConfigurationPtrOutput {
	return o
}

func (o MapConfigurationPtrOutput) Elem() MapConfigurationOutput {
	return o.ApplyT(func(v *MapConfiguration) MapConfiguration {
		if v != nil {
			return *v
		}
		var ret MapConfiguration
		return ret
	}).(MapConfigurationOutput)
}

func (o MapConfigurationPtrOutput) Style() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MapConfiguration) *string {
		if v == nil {
			return nil
		}
		return &v.Style
	}).(pulumi.StringPtrOutput)
}

type PlaceIndexDataSourceConfiguration struct {
	IntendedUse *PlaceIndexIntendedUse `pulumi:"intendedUse"`
}

// PlaceIndexDataSourceConfigurationInput is an input type that accepts PlaceIndexDataSourceConfigurationArgs and PlaceIndexDataSourceConfigurationOutput values.
// You can construct a concrete instance of `PlaceIndexDataSourceConfigurationInput` via:
//
//          PlaceIndexDataSourceConfigurationArgs{...}
type PlaceIndexDataSourceConfigurationInput interface {
	pulumi.Input

	ToPlaceIndexDataSourceConfigurationOutput() PlaceIndexDataSourceConfigurationOutput
	ToPlaceIndexDataSourceConfigurationOutputWithContext(context.Context) PlaceIndexDataSourceConfigurationOutput
}

type PlaceIndexDataSourceConfigurationArgs struct {
	IntendedUse PlaceIndexIntendedUsePtrInput `pulumi:"intendedUse"`
}

func (PlaceIndexDataSourceConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PlaceIndexDataSourceConfiguration)(nil)).Elem()
}

func (i PlaceIndexDataSourceConfigurationArgs) ToPlaceIndexDataSourceConfigurationOutput() PlaceIndexDataSourceConfigurationOutput {
	return i.ToPlaceIndexDataSourceConfigurationOutputWithContext(context.Background())
}

func (i PlaceIndexDataSourceConfigurationArgs) ToPlaceIndexDataSourceConfigurationOutputWithContext(ctx context.Context) PlaceIndexDataSourceConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PlaceIndexDataSourceConfigurationOutput)
}

func (i PlaceIndexDataSourceConfigurationArgs) ToPlaceIndexDataSourceConfigurationPtrOutput() PlaceIndexDataSourceConfigurationPtrOutput {
	return i.ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(context.Background())
}

func (i PlaceIndexDataSourceConfigurationArgs) ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(ctx context.Context) PlaceIndexDataSourceConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PlaceIndexDataSourceConfigurationOutput).ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(ctx)
}

// PlaceIndexDataSourceConfigurationPtrInput is an input type that accepts PlaceIndexDataSourceConfigurationArgs, PlaceIndexDataSourceConfigurationPtr and PlaceIndexDataSourceConfigurationPtrOutput values.
// You can construct a concrete instance of `PlaceIndexDataSourceConfigurationPtrInput` via:
//
//          PlaceIndexDataSourceConfigurationArgs{...}
//
//  or:
//
//          nil
type PlaceIndexDataSourceConfigurationPtrInput interface {
	pulumi.Input

	ToPlaceIndexDataSourceConfigurationPtrOutput() PlaceIndexDataSourceConfigurationPtrOutput
	ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(context.Context) PlaceIndexDataSourceConfigurationPtrOutput
}

type placeIndexDataSourceConfigurationPtrType PlaceIndexDataSourceConfigurationArgs

func PlaceIndexDataSourceConfigurationPtr(v *PlaceIndexDataSourceConfigurationArgs) PlaceIndexDataSourceConfigurationPtrInput {
	return (*placeIndexDataSourceConfigurationPtrType)(v)
}

func (*placeIndexDataSourceConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**PlaceIndexDataSourceConfiguration)(nil)).Elem()
}

func (i *placeIndexDataSourceConfigurationPtrType) ToPlaceIndexDataSourceConfigurationPtrOutput() PlaceIndexDataSourceConfigurationPtrOutput {
	return i.ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(context.Background())
}

func (i *placeIndexDataSourceConfigurationPtrType) ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(ctx context.Context) PlaceIndexDataSourceConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PlaceIndexDataSourceConfigurationPtrOutput)
}

type PlaceIndexDataSourceConfigurationOutput struct{ *pulumi.OutputState }

func (PlaceIndexDataSourceConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PlaceIndexDataSourceConfiguration)(nil)).Elem()
}

func (o PlaceIndexDataSourceConfigurationOutput) ToPlaceIndexDataSourceConfigurationOutput() PlaceIndexDataSourceConfigurationOutput {
	return o
}

func (o PlaceIndexDataSourceConfigurationOutput) ToPlaceIndexDataSourceConfigurationOutputWithContext(ctx context.Context) PlaceIndexDataSourceConfigurationOutput {
	return o
}

func (o PlaceIndexDataSourceConfigurationOutput) ToPlaceIndexDataSourceConfigurationPtrOutput() PlaceIndexDataSourceConfigurationPtrOutput {
	return o.ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(context.Background())
}

func (o PlaceIndexDataSourceConfigurationOutput) ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(ctx context.Context) PlaceIndexDataSourceConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v PlaceIndexDataSourceConfiguration) *PlaceIndexDataSourceConfiguration {
		return &v
	}).(PlaceIndexDataSourceConfigurationPtrOutput)
}

func (o PlaceIndexDataSourceConfigurationOutput) IntendedUse() PlaceIndexIntendedUsePtrOutput {
	return o.ApplyT(func(v PlaceIndexDataSourceConfiguration) *PlaceIndexIntendedUse { return v.IntendedUse }).(PlaceIndexIntendedUsePtrOutput)
}

type PlaceIndexDataSourceConfigurationPtrOutput struct{ *pulumi.OutputState }

func (PlaceIndexDataSourceConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PlaceIndexDataSourceConfiguration)(nil)).Elem()
}

func (o PlaceIndexDataSourceConfigurationPtrOutput) ToPlaceIndexDataSourceConfigurationPtrOutput() PlaceIndexDataSourceConfigurationPtrOutput {
	return o
}

func (o PlaceIndexDataSourceConfigurationPtrOutput) ToPlaceIndexDataSourceConfigurationPtrOutputWithContext(ctx context.Context) PlaceIndexDataSourceConfigurationPtrOutput {
	return o
}

func (o PlaceIndexDataSourceConfigurationPtrOutput) Elem() PlaceIndexDataSourceConfigurationOutput {
	return o.ApplyT(func(v *PlaceIndexDataSourceConfiguration) PlaceIndexDataSourceConfiguration {
		if v != nil {
			return *v
		}
		var ret PlaceIndexDataSourceConfiguration
		return ret
	}).(PlaceIndexDataSourceConfigurationOutput)
}

func (o PlaceIndexDataSourceConfigurationPtrOutput) IntendedUse() PlaceIndexIntendedUsePtrOutput {
	return o.ApplyT(func(v *PlaceIndexDataSourceConfiguration) *PlaceIndexIntendedUse {
		if v == nil {
			return nil
		}
		return v.IntendedUse
	}).(PlaceIndexIntendedUsePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(MapConfigurationOutput{})
	pulumi.RegisterOutputType(MapConfigurationPtrOutput{})
	pulumi.RegisterOutputType(PlaceIndexDataSourceConfigurationOutput{})
	pulumi.RegisterOutputType(PlaceIndexDataSourceConfigurationPtrOutput{})
}
